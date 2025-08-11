from django.db import models
from django.utils import timezone

class Tabuleiro(models.Model):
    """Modelo para representar o tabuleiro do jogo da velha"""
    linha = models.IntegerField()
    coluna = models.IntegerField()
    valor = models.CharField(max_length=1, choices=[('X', 'X'), ('O', 'O')])
    data_criacao = models.DateTimeField(default=timezone.now)
    
    class Meta:
        unique_together = ['linha', 'coluna']
        db_table = 'tabuleiro'
    
    def __str__(self):
        return f"({self.linha}, {self.coluna}) = {self.valor}"

class Partida(models.Model):
    """Modelo para controlar o estado da partida"""
    modo_jogo = models.CharField(
        max_length=20, 
        choices=[
            ('single', 'Jogar Sozinho'),
            ('multi', 'Multijogador Local')
        ],
        default='multi'
    )
    jogador_atual = models.CharField(max_length=1, default='X')
    ativo = models.BooleanField(default=True)
    vencedor = models.CharField(max_length=1, blank=True, null=True)
    empate = models.BooleanField(default=False)
    data_inicio = models.DateTimeField(default=timezone.now)
    data_fim = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        db_table = 'partida'
    
    def __str__(self):
        return f"Partida {self.id} - {self.modo_jogo} - {'Ativa' if self.ativo else 'Finalizada'}"
    
    def resetar_tabuleiro(self):
        """Remove todas as jogadas do tabuleiro"""
        Tabuleiro.objects.all().delete()
        self.jogador_atual = 'X'
        self.vencedor = None
        self.empate = False
        self.ativo = True
        self.data_inicio = timezone.now()
        self.data_fim = None
        self.save()
    
    def verificar_vitoria(self):
        """Verifica se há um vencedor na partida"""
        # Obter todas as posições do tabuleiro
        posicoes = {}
        for tab in Tabuleiro.objects.all():
            posicoes[(tab.linha, tab.coluna)] = tab.valor
        
        # Verificar linhas horizontais
        for linha in range(3):
            if all((linha, col) in posicoes for col in range(3)):
                if posicoes[(linha, 0)] == posicoes[(linha, 1)] == posicoes[(linha, 2)]:
                    return posicoes[(linha, 0)]
        
        # Verificar colunas verticais
        for col in range(3):
            if all((linha, col) in posicoes for linha in range(3)):
                if posicoes[(0, col)] == posicoes[(1, col)] == posicoes[(2, col)]:
                    return posicoes[(0, col)]
        
        # Verificar diagonais
        if all((i, i) in posicoes for i in range(3)):
            if posicoes[(0, 0)] == posicoes[(1, 1)] == posicoes[(2, 2)]:
                return posicoes[(0, 0)]
        
        if all((i, 2-i) in posicoes for i in range(3)):
            if posicoes[(0, 2)] == posicoes[(1, 1)] == posicoes[(2, 0)]:
                return posicoes[(0, 2)]
        
        return None
    
    def verificar_empate(self):
        """Verifica se a partida terminou em empate"""
        return Tabuleiro.objects.count() == 9
    
    def proximo_jogador(self):
        """Alterna para o próximo jogador"""
        self.jogador_atual = 'O' if self.jogador_atual == 'X' else 'X'
        self.save()
    
    def finalizar_partida(self, vencedor=None, empate=False):
        """Finaliza a partida"""
        self.ativo = False
        self.vencedor = vencedor
        self.empate = empate
        self.data_fim = timezone.now()
        self.save()
