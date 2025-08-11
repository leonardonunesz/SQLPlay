from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
import re
import random
from .models import Tabuleiro, Partida

def jogo_da_velha(request):
    """View para o jogo da velha"""
    # Criar ou obter partida ativa
    partida, created = Partida.objects.get_or_create(
        ativo=True,
        defaults={'modo_jogo': 'multi'}
    )
    
    # Obter estado atual do tabuleiro
    tabuleiro_data = {}
    for tab in Tabuleiro.objects.all():
        tabuleiro_data[f"{tab.linha}_{tab.coluna}"] = tab.valor
    
    context = {
        'titulo': 'Jogo da Velha - SQLPlay',
        'descricao': 'Use comandos SQL para jogar! Digite INSERT ou UPDATE para fazer suas jogadas.',
        'partida_id': partida.id,
        'jogador_atual': partida.jogador_atual,
        'modo_jogo': partida.modo_jogo,
        'tabuleiro': tabuleiro_data,
        'partida_ativa': partida.ativo
    }
    return render(request, 'jogo_da_velha/jogo.html', context)

@csrf_exempt
@require_http_methods(["POST"])
def executar_sql(request):
    """Executa comandos SQL e retorna o resultado"""
    try:
        data = json.loads(request.body)
        comando_sql = data.get('comando', '').strip()
        
        if not comando_sql:
            return JsonResponse({
                'success': False,
                'error': 'Comando SQL não fornecido'
            })
        
        # Processar comando SQL
        resultado = processar_comando_sql(comando_sql)
        
        if resultado['success']:
            # Atualizar o tabuleiro no banco
            linha = resultado['linha']
            coluna = resultado['coluna']
            valor = resultado['valor']
            
            # Verificar se a posição já está ocupada
            if Tabuleiro.objects.filter(linha=linha, coluna=coluna).exists():
                return JsonResponse({
                    'success': False,
                    'error': 'Esta posição já está ocupada!'
                })
            
            # Criar a jogada
            Tabuleiro.objects.create(linha=linha, coluna=coluna, valor=valor)
            
            # Obter partida ativa
            partida = Partida.objects.get(ativo=True)
            
            # Verificar vitória
            vencedor = partida.verificar_vitoria()
            if vencedor:
                partida.finalizar_partida(vencedor=vencedor)
                return JsonResponse({
                    'success': True,
                    'message': f'Jogador {valor} venceu!',
                    'jogada_valida': True,
                    'jogo_finalizado': True,
                    'vencedor': vencedor,
                    'tabuleiro': get_tabuleiro_data()
                })
            
            # Verificar empate
            if partida.verificar_empate():
                partida.finalizar_partida(empate=True)
                return JsonResponse({
                    'success': True,
                    'message': 'Empate!',
                    'jogada_valida': True,
                    'jogo_finalizado': True,
                    'empate': True,
                    'tabuleiro': get_tabuleiro_data()
                })
            
            # Se for modo single player e for vez do computador
            if partida.modo_jogo == 'single' and valor == 'X':
                # Alternar para jogador O (computador)
                partida.proximo_jogador()
                
                # Fazer jogada do computador
                jogada_computador = fazer_jogada_computador()
                if jogada_computador:
                    # Verificar vitória do computador
                    vencedor = partida.verificar_vitoria()
                    if vencedor:
                        partida.finalizar_partida(vencedor=vencedor)
                        return JsonResponse({
                            'success': True,
                            'message': 'Computador venceu!',
                            'jogada_valida': True,
                            'jogo_finalizado': True,
                            'vencedor': vencedor,
                            'jogada_computador': jogada_computador,
                            'tabuleiro': get_tabuleiro_data()
                        })
                    
                    # Verificar empate
                    if partida.verificar_empate():
                        partida.finalizar_partida(empate=True)
                        return JsonResponse({
                            'success': True,
                            'message': 'Empate!',
                            'jogada_valida': True,
                            'jogo_finalizado': True,
                            'empate': True,
                            'jogada_computador': jogada_computador,
                            'tabuleiro': get_tabuleiro_data()
                        })
                    
                    # Alternar para jogador X
                    partida.proximo_jogador()
                    
                    return JsonResponse({
                        'success': True,
                        'message': 'Jogada válida! Computador fez sua jogada.',
                        'jogada_valida': True,
                        'jogada_computador': jogada_computador,
                        'jogador_atual': partida.jogador_atual,
                        'tabuleiro': get_tabuleiro_data()
                    })
            
            # Alternar jogador para modo multijogador
            if partida.modo_jogo == 'multi':
                partida.proximo_jogador()
            
            return JsonResponse({
                'success': True,
                'message': 'Jogada válida!',
                'jogada_valida': True,
                'jogador_atual': partida.jogador_atual,
                'tabuleiro': get_tabuleiro_data()
            })
        
        else:
            return JsonResponse({
                'success': False,
                'error': resultado['error']
            })
            
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': f'Erro ao processar comando: {str(e)}'
        })

def processar_comando_sql(comando):
    """Processa e valida comandos SQL"""
    comando = comando.strip().lower()
    
    # Padrões para INSERT
    insert_pattern = r'insert\s+into\s+tabuleiro\s*\([^)]*\)\s+values\s*\(([^)]+)\)'
    insert_match = re.search(insert_pattern, comando, re.IGNORECASE)
    
    if insert_match:
        try:
            values = insert_match.group(1).split(',')
            if len(values) >= 3:
                linha = int(values[0].strip().replace("'", "").replace('"', ''))
                coluna = int(values[1].strip().replace("'", "").replace('"', ''))
                valor = values[2].strip().replace("'", "").replace('"', '').upper()
                
                if validar_jogada(linha, coluna, valor):
                    return {'success': True, 'linha': linha, 'coluna': coluna, 'valor': valor}
        except (ValueError, IndexError):
            pass
    
    # Padrões para UPDATE
    update_pattern = r'update\s+tabuleiro\s+set\s+valor\s*=\s*["\']([XO])["\']\s+where\s+linha\s*=\s*(\d+)\s+and\s+coluna\s*=\s*(\d+)'
    update_match = re.search(update_pattern, comando, re.IGNORECASE)
    
    if update_match:
        try:
            valor = update_match.group(1).upper()
            linha = int(update_match.group(2))
            coluna = int(update_match.group(3))
            
            if validar_jogada(linha, coluna, valor):
                return {'success': True, 'linha': linha, 'coluna': coluna, 'valor': valor}
        except (ValueError, IndexError):
            pass
    
    return {
        'success': False,
        'error': 'Comando SQL inválido. Use INSERT ou UPDATE com valores válidos (linha: 0-2, coluna: 0-2, valor: X ou O)'
    }

def validar_jogada(linha, coluna, valor):
    """Valida se uma jogada é válida"""
    return (
        0 <= linha <= 2 and 
        0 <= coluna <= 2 and 
        valor in ['X', 'O']
    )

def fazer_jogada_computador():
    """Faz uma jogada aleatória para o computador"""
    # Encontrar posições vazias
    posicoes_ocupadas = set()
    for tab in Tabuleiro.objects.all():
        posicoes_ocupadas.add((tab.linha, tab.coluna))
    
    posicoes_vazias = []
    for linha in range(3):
        for coluna in range(3):
            if (linha, coluna) not in posicoes_ocupadas:
                posicoes_vazias.append((linha, coluna))
    
    if posicoes_vazias:
        # Escolher posição aleatória
        linha, coluna = random.choice(posicoes_vazias)
        valor = 'O'
        
        # Criar a jogada
        Tabuleiro.objects.create(linha=linha, coluna=coluna, valor=valor)
        
        return {'linha': linha, 'coluna': coluna, 'valor': valor}
    
    return None

def get_tabuleiro_data():
    """Retorna o estado atual do tabuleiro"""
    tabuleiro_data = {}
    for tab in Tabuleiro.objects.all():
        tabuleiro_data[f"{tab.linha}_{tab.coluna}"] = tab.valor
    return tabuleiro_data

@csrf_exempt
@require_http_methods(["POST"])
def novo_jogo(request):
    """Inicia um novo jogo"""
    try:
        data = json.loads(request.body)
        modo_jogo = data.get('modo', 'multi')
        
        # Finalizar partida atual se existir
        if Partida.objects.filter(ativo=True).exists():
            partida_atual = Partida.objects.get(ativo=True)
            partida_atual.ativo = False
            partida_atual.save()
        
        # Criar nova partida
        nova_partida = Partida.objects.create(modo_jogo=modo_jogo)
        
        # Limpar tabuleiro
        Tabuleiro.objects.all().delete()
        
        return JsonResponse({
            'success': True,
            'message': 'Novo jogo iniciado!',
            'partida_id': nova_partida.id,
            'jogador_atual': nova_partida.jogador_atual,
            'modo_jogo': nova_partida.modo_jogo,
            'tabuleiro': {}
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': f'Erro ao iniciar novo jogo: {str(e)}'
        })

@csrf_exempt
@require_http_methods(["GET"])
def obter_estado_jogo(request):
    """Retorna o estado atual do jogo"""
    try:
        partida = Partida.objects.filter(ativo=True).first()
        if not partida:
            return JsonResponse({
                'success': False,
                'error': 'Nenhuma partida ativa encontrada'
            })
        
        return JsonResponse({
            'success': True,
            'partida_id': partida.id,
            'jogador_atual': partida.jogador_atual,
            'modo_jogo': partida.modo_jogo,
            'tabuleiro': get_tabuleiro_data(),
            'partida_ativa': partida.ativo
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': f'Erro ao obter estado do jogo: {str(e)}'
        })
