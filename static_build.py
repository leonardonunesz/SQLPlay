#!/usr/bin/env python3
"""
Script para gerar versão estática do Django para GitHub Pages
"""

import os
import sys
import django
from pathlib import Path

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sqlplay.settings')
django.setup()

from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.staticfiles import finders
from django.contrib.staticfiles.storage import staticfiles_storage
import shutil

def build_static_site():
    """Constrói uma versão estática do site Django"""
    
    # Diretório de saída
    output_dir = Path('./static_site')
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir()
    
    # Copiar arquivos estáticos
    static_dir = output_dir / 'static'
    static_dir.mkdir()
    
    # Copiar CSS, JS e outros arquivos estáticos
    for static_file in Path('./static').rglob('*'):
        if static_file.is_file():
            relative_path = static_file.relative_to('./static')
            dest_path = static_dir / relative_path
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(static_file, dest_path)
    
    # Gerar página inicial estática
    home_content = render_to_string('home.html', {})
    
    # Substituir tags Django por conteúdo estático
    home_content = home_content.replace('{% load static %}', '')
    home_content = home_content.replace('{% url "jogo_da_velha:jogo_da_velha" %}', './jogo-da-velha.html')
    
    # Salvar página inicial
    with open(output_dir / 'index.html', 'w', encoding='utf-8') as f:
        f.write(home_content)
    
    # Gerar página do jogo da velha estática
    jogo_content = render_to_string('jogo_da_velha/jogo.html', {
        'partida_ativa': None,
        'modo_jogo': None,
        'jogador_atual': None,
        'tabuleiro': []
    })
    
    # Substituir tags Django
    jogo_content = jogo_content.replace('{% load static %}', '')
    jogo_content = jogo_content.replace('{% static "css/jogo_da_velha.css" %}', './static/css/jogo_da_velha.css')
    jogo_content = jogo_content.replace('{% static "js/jogo_da_velha.js" %}', './static/js/jogo_da_velha.js')
    
    # Salvar página do jogo
    with open(output_dir / 'jogo-da-velha.html', 'w', encoding='utf-8') as f:
        f.write(jogo_content)
    
    # Criar arquivo .nojekyll para GitHub Pages
    with open(output_dir / '.nojekyll', 'w') as f:
        pass
    
    print(f"Site estático gerado em: {output_dir.absolute()}")
    print("Arquivos criados:")
    for file_path in output_dir.rglob('*'):
        if file_path.is_file():
            print(f"  - {file_path.relative_to(output_dir)}")

if __name__ == '__main__':
    build_static_site()
