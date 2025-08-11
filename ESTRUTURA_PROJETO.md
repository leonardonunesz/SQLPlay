# Estrutura do Projeto SQLPlay

## Visão Geral da Organização

Este documento descreve a estrutura organizada do projeto SQLPlay, explicando a função de cada arquivo e pasta para facilitar o entendimento de desenvolvedores que queiram contribuir ou entender como o projeto funciona.

## Estrutura de Arquivos e Pastas

```
SQLPlay/
├── static/                          # Arquivos estáticos do projeto
│   ├── css/                         # Folhas de estilo CSS
│   │   ├── style.css               # Estilos globais e da página inicial
│   │   └── jogo_da_velha.css      # Estilos específicos do jogo da velha
│   ├── js/                         # Scripts JavaScript
│   │   └── jogo_da_velha.js       # Lógica JavaScript do jogo da velha
│   └── img/                        # Imagens, ícones e recursos visuais
├── templates/                       # Templates HTML do Django
│   ├── core/                       # Templates da aplicação principal
│   │   └── home.html               # Página inicial com seleção de jogos
│   └── jogo_da_velha/             # Templates específicos do jogo
│       └── jogo.html               # Interface principal do jogo da velha
├── core/                           # Aplicação Django principal
│   ├── __init__.py                 # Inicialização do app core
│   ├── admin.py                    # Configurações do admin Django
│   ├── apps.py                     # Configuração da aplicação core
│   ├── models.py                   # Modelos de dados da aplicação principal
│   ├── tests.py                    # Testes unitários do app core
│   ├── urls.py                     # Roteamento de URLs da aplicação principal
│   └── views.py                    # Lógica de negócio e renderização das páginas
├── jogo_da_velha/                  # Aplicação Django do jogo da velha
│   ├── __init__.py                 # Inicialização do app jogo_da_velha
│   ├── admin.py                    # Configurações do admin para o jogo
│   ├── apps.py                     # Configuração da aplicação jogo_da_velha
│   ├── models.py                   # Modelos de dados do jogo (Partida, Tabuleiro)
│   ├── tests.py                    # Testes unitários do jogo
│   ├── urls.py                     # Roteamento de URLs específicas do jogo
│   └── views.py                    # Lógica de negócio e API endpoints do jogo
├── sqlplay/                        # Configurações principais do projeto Django
│   ├── __init__.py                 # Inicialização do projeto
│   ├── asgi.py                     # Configuração ASGI para produção
│   ├── settings.py                 # Configurações do Django (apps, banco, etc.)
│   ├── urls.py                     # Roteamento principal de URLs do projeto
│   └── wsgi.py                     # Configuração WSGI para produção
├── venv/                           # Ambiente virtual Python (não versionado)
├── .gitignore                      # Arquivos e pastas ignorados pelo Git
├── db.sqlite3                      # Banco de dados SQLite (desenvolvimento)
├── ESTRUTURA_PROJETO.md            # Este arquivo de documentação
├── manage.py                       # Script de gerenciamento do Django
├── README.md                       # Documentação principal do projeto
└── requirements.txt                # Dependências Python do projeto
```

## Explicação Detalhada de Cada Área

### 1. Pasta `static/` - Arquivos Estáticos

#### `static/css/`
- **`style.css`**: Contém estilos globais aplicados em todo o projeto, incluindo layout da página inicial, componentes comuns como botões, cards de jogos e responsividade geral.
- **`jogo_da_velha.css`**: Estilos específicos do jogo da velha, incluindo layout do tabuleiro, modais, botões específicos do jogo e responsividade detalhada para diferentes tamanhos de tela.

#### `static/js/`
- **`jogo_da_velha.js`**: Contém toda a lógica JavaScript do jogo, incluindo seleção de modo de jogo, execução de comandos SQL via AJAX, atualização do tabuleiro, gerenciamento de modais e comunicação com o backend Django.

#### `static/img/`
- Armazena imagens, ícones e recursos visuais utilizados no projeto.

### 2. Pasta `templates/` - Templates HTML

#### `templates/core/`
- **`home.html`**: Template da página inicial que apresenta os jogos disponíveis, com cards para cada jogo e navegação para as diferentes funcionalidades.

#### `templates/jogo_da_velha/`
- **`jogo.html`**: Template principal do jogo da velha, contendo o tabuleiro 3x3, interface de input SQL, modais de resultado e ajuda, e toda a estrutura HTML necessária para o funcionamento do jogo.

### 3. Pasta `core/` - Aplicação Principal

#### `core/__init__.py`
- Arquivo vazio que marca o diretório como um pacote Python, permitindo que o Django reconheça esta pasta como uma aplicação.

#### `core/admin.py`
- Configurações do painel administrativo do Django para a aplicação principal, permitindo gerenciar dados através da interface admin.

#### `core/apps.py`
- Configuração da aplicação core, definindo seu nome e configurações específicas.

#### `core/models.py`
- Define os modelos de dados da aplicação principal, se houver algum.

#### `core/tests.py`
- Arquivo para testes unitários da aplicação principal.

#### `core/urls.py`
- Define as rotas de URL da aplicação principal, mapeando URLs para as views correspondentes.

#### `core/views.py`
- Contém a lógica de negócio para renderizar a página inicial e outras funcionalidades da aplicação principal.

### 4. Pasta `jogo_da_velha/` - Aplicação do Jogo

#### `jogo_da_velha/__init__.py`
- Arquivo vazio que marca o diretório como um pacote Python.

#### `jogo_da_velha/admin.py`
- Configurações do admin para gerenciar partidas e tabuleiros do jogo.

#### `jogo_da_velha/apps.py`
- Configuração da aplicação jogo_da_velha.

#### `jogo_da_velha/models.py`
- Define os modelos de dados do jogo:
  - **`Partida`**: Representa uma partida completa, com informações sobre modo de jogo, jogador atual, status e resultado.
  - **`Tabuleiro`**: Representa cada jogada individual, com coordenadas (linha, coluna) e valor (X ou O).

#### `jogo_da_velha/tests.py`
- Testes unitários específicos do jogo da velha.

#### `jogo_da_velha/urls.py`
- Define as rotas de URL específicas do jogo, incluindo endpoints da API para executar SQL, iniciar novos jogos e obter estado atual.

#### `jogo_da_velha/views.py`
- Contém toda a lógica de negócio do jogo:
  - **`jogo_da_velha`**: Renderiza o template principal do jogo.
  - **`executar_sql`**: Processa comandos SQL, valida jogadas e atualiza o estado do jogo.
  - **`novo_jogo`**: Inicia uma nova partida, limpando o tabuleiro anterior.
  - **`obter_estado_jogo`**: Retorna o estado atual do jogo para o frontend.

### 5. Pasta `sqlplay/` - Configurações do Projeto

#### `sqlplay/__init__.py`
- Arquivo vazio que marca o diretório como um pacote Python.

#### `sqlplay/asgi.py`
- Configuração ASGI para execução em produção com servidores assíncronos.

#### `sqlplay/settings.py`
- Arquivo principal de configuração do Django, incluindo:
  - Aplicações instaladas (`INSTALLED_APPS`)
  - Configurações de banco de dados
  - Configurações de arquivos estáticos
  - Configurações de segurança e debug

#### `sqlplay/urls.py`
- Roteamento principal de URLs do projeto, incluindo redirecionamentos para as diferentes aplicações.

#### `sqlplay/wsgi.py`
- Configuração WSGI para execução em produção com servidores tradicionais.

### 6. Arquivos de Configuração

#### `.gitignore`
- Define quais arquivos e pastas devem ser ignorados pelo controle de versão Git, incluindo ambiente virtual, banco de dados e arquivos temporários.

#### `db.sqlite3`
- Banco de dados SQLite usado em desenvolvimento. Em produção, seria substituído por MySQL ou PostgreSQL.

#### `ESTRUTURA_PROJETO.md`
- Este arquivo de documentação, explicando a estrutura e funcionamento do projeto.

#### `manage.py`
- Script de linha de comando do Django para executar operações como rodar servidor, criar migrações, executar testes, etc.

#### `README.md`
- Documentação principal do projeto, explicando funcionalidades, instalação e uso.

#### `requirements.txt`
- Lista todas as dependências Python necessárias para executar o projeto, com versões específicas.

## Como Funciona a Arquitetura

### Fluxo de Requisições
1. **URL Request**: Usuário acessa uma URL (ex: `/jogo-da-velha/`)
2. **URL Routing**: `sqlplay/urls.py` direciona para a aplicação correta
3. **App URLs**: A aplicação específica (`jogo_da_velha/urls.py`) mapeia para a view correta
4. **View Processing**: A view processa a requisição, interage com modelos e renderiza templates
5. **Template Rendering**: O template HTML é renderizado com dados do contexto
6. **Response**: A resposta HTML é enviada para o navegador

### Separação de Responsabilidades
- **Models**: Definem a estrutura de dados e regras de negócio
- **Views**: Processam requisições e coordenam entre models e templates
- **Templates**: Definem a apresentação visual e estrutura HTML
- **URLs**: Mapeiam URLs para views específicas
- **Static Files**: Fornecem CSS, JavaScript e recursos visuais

### Padrões de Desenvolvimento
- **MVC Pattern**: Django segue o padrão Model-View-Template
- **App-based Architecture**: Funcionalidades são organizadas em aplicações separadas
- **Separation of Concerns**: CSS, JavaScript e HTML são mantidos em arquivos separados
- **Responsive Design**: Interface adaptável para diferentes dispositivos
- **API-first Approach**: Backend fornece endpoints JSON para comunicação com frontend

## Benefícios da Organização

### Manutenibilidade
- Código organizado por funcionalidade
- Fácil localização de problemas
- Separação clara de responsabilidades

### Escalabilidade
- Novos jogos seguem o mesmo padrão
- Estrutura modular permite crescimento
- Componentes reutilizáveis

### Performance
- Arquivos estáticos podem ser cacheados
- Carregamento paralelo de recursos
- Minificação futura facilitada

### Colaboração
- Múltiplos desenvolvedores podem trabalhar simultaneamente
- Estrutura clara para novos contribuidores
- Padrões consistentes de código

## Como Adicionar Novos Jogos

### 1. Criar Nova Aplicação Django
```bash
python manage.py startapp novo_jogo
```

### 2. Adicionar ao settings.py
```python
INSTALLED_APPS = [
    # ... outras apps
    'novo_jogo',
]
```

### 3. Criar Estrutura de Arquivos
```
novo_jogo/
├── static/css/novo_jogo.css
├── static/js/novo_jogo.js
├── templates/novo_jogo/jogo.html
├── models.py
├── views.py
└── urls.py
```

### 4. Seguir Padrões Estabelecidos
- Usar mesma estrutura de CSS e JavaScript
- Implementar responsividade
- Seguir convenções de nomenclatura
- Documentar funcionalidades

## Convenções de Código

### Nomenclatura
- **Arquivos Python**: snake_case (ex: `views.py`)
- **Classes Python**: PascalCase (ex: `Partida`)
- **Funções Python**: snake_case (ex: `executar_sql`)
- **Variáveis Python**: snake_case (ex: `jogador_atual`)
- **Classes CSS**: kebab-case (ex: `game-container`)
- **IDs HTML**: snake_case (ex: `modeSelection`)

### Organização
- **CSS**: Organizado por funcionalidade e responsividade
- **JavaScript**: Funções agrupadas por responsabilidade
- **HTML**: Estrutura semântica e acessível
- **Python**: Imports organizados, docstrings para funções complexas

---

**Última Atualização**: Janeiro 2025  
**Desenvolvido por**: [@leonardonunesz](https://github.com/leonardonunesz)  
**Objetivo**: Aprender SQL através de jogos interativos
