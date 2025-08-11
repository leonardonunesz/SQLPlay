# 📁 Estrutura Organizada do Projeto SQLPlay

## 🎯 **Visão Geral da Organização**

Este documento descreve a nova estrutura organizada do projeto SQLPlay, onde separamos CSS, JavaScript e HTML em arquivos distintos para melhor manutenção e organização.

## 🗂️ **Estrutura de Arquivos**

```
SQLPlay/
├── 📁 static/                          # Arquivos estáticos
│   ├── 📁 css/                         # Folhas de estilo
│   │   ├── style.css                   # Estilos globais (home + geral)
│   │   └── jogo_da_velha.css          # Estilos específicos do jogo
│   ├── 📁 js/                          # Scripts JavaScript
│   │   └── jogo_da_velha.js           # Lógica do jogo da velha
│   └── 📁 img/                         # Imagens e ícones
├── 📁 templates/                       # Templates HTML
│   ├── 📁 core/                        # Templates do app core
│   │   └── home.html                   # Página inicial
│   └── 📁 jogo_da_velha/              # Templates do jogo
│       └── jogo.html                   # Template do jogo da velha
├── 📁 core/                            # App principal
├── 📁 jogo_da_velha/                   # App do jogo da velha
├── 📁 sqlplay/                         # Configurações do projeto
└── 📄 manage.py                        # Gerenciador Django
```

## 🎨 **Separação de Responsabilidades**

### **1. CSS (Cascading Style Sheets)**

- **`static/css/style.css`**: Estilos globais e da página inicial
- **`static/css/jogo_da_velha.css`**: Estilos específicos do jogo da velha
  - Layout do tabuleiro
  - Estilos dos modais
  - Responsividade completa
  - Animações e transições

### **2. JavaScript**

- **`static/js/jogo_da_velha.js`**: Toda a lógica do jogo
  - Seleção de modo de jogo
  - Execução de comandos SQL
  - Atualização do tabuleiro
  - Gerenciamento de modais
  - Comunicação com o backend

### **3. HTML**

- **`templates/jogo_da_velha/jogo.html`**: Template limpo e organizado
  - Estrutura semântica
  - Imports de CSS e JS externos
  - Sem código inline
  - Fácil manutenção

## 🚀 **Benefícios da Nova Estrutura**

### ✅ **Manutenibilidade**

- **Código separado** por responsabilidade
- **Fácil localização** de problemas
- **Reutilização** de estilos e scripts

### ✅ **Performance**

- **Cache do navegador** para arquivos estáticos
- **Carregamento paralelo** de CSS e JS
- **Minificação** futura facilitada

### ✅ **Desenvolvimento**

- **Edição simultânea** por equipes
- **Controle de versão** mais eficiente
- **Debugging** simplificado

### ✅ **Escalabilidade**

- **Novos jogos** seguem o mesmo padrão
- **Componentes reutilizáveis**
- **Arquitetura modular**

## 🔧 **Como Usar**

### **1. Adicionar Novo CSS**

```html
<!-- No template HTML -->
<link rel="stylesheet" href="{% static 'css/novo_jogo.css' %}" />
```

### **2. Adicionar Novo JavaScript**

```html
<!-- No template HTML -->
<script src="{% static 'js/novo_jogo.js' %}"></script>
```

### **3. Criar Novo Jogo**

1. Criar pasta `static/css/novo_jogo.css`
2. Criar pasta `static/js/novo_jogo.js`
3. Criar template `templates/novo_jogo/jogo.html`
4. Seguir o padrão de organização

## 📱 **Responsividade**

### **Breakpoints Implementados**

- **Desktop**: `> 768px` - Layout completo
- **Tablet**: `≤ 768px` - Ajustes de tamanho
- **Mobile**: `≤ 480px` - Layout otimizado
- **Small Mobile**: `≤ 360px` - Layout compacto
- **Landscape**: `≤ 500px height` - Orientação horizontal

### **Elementos Responsivos**

- Tabuleiro do jogo
- Botões e inputs
- Modais e overlays
- Tipografia e espaçamentos

## 🎮 **Funcionalidades do Jogo**

### **Modos de Jogo**

- **Multijogador Local**: Dois jogadores alternando turnos
- **Contra Computador**: Jogador vs IA com movimentos aleatórios

### **Sistema SQL**

- **Comandos aceitos**: `INSERT INTO` e `UPDATE`
- **Validação**: Sintaxe e regras do jogo
- **Feedback**: Mensagens de erro e sucesso

### **Interface**

- **Seleção de modo** no início
- **Tabuleiro interativo** 3x3
- **Input SQL** com validação
- **Modais informativos** para resultado e ajuda

## 🛠️ **Tecnologias Utilizadas**

- **Backend**: Django (Python)
- **Frontend**: HTML5, CSS3, JavaScript ES6+
- **Database**: SQLite (desenvolvimento) / MySQL (produção)
- **Responsividade**: CSS Grid, Flexbox, Media Queries
- **Ícones**: Font Awesome 6.0
- **Fontes**: Google Fonts (Inter)

## 📝 **Convenções de Código**

### **CSS**

- **Classes**: kebab-case (ex: `game-container`)
- **Organização**: Por funcionalidade e responsividade
- **Comentários**: Seções claramente marcadas

### **JavaScript**

- **Funções**: camelCase (ex: `selecionarModo`)
- **Variáveis**: camelCase (ex: `jogadorAtual`)
- **Constantes**: UPPER_SNAKE_CASE (se aplicável)

### **HTML**

- **IDs**: snake_case (ex: `modeSelection`)
- **Classes**: kebab-case (ex: `mode-button`)
- **Estrutura**: Semântica e acessível

## 🔮 **Próximos Passos**

1. **Implementar novos jogos** seguindo o padrão
2. **Adicionar testes** para CSS e JavaScript
3. **Otimizar performance** com minificação
4. **Implementar PWA** para instalação mobile
5. **Adicionar temas** (claro/escuro)

---

**📅 Última Atualização**: Janeiro 2025  
**👨‍💻 Desenvolvido por**: Equipe SQLPlay  
**🎯 Objetivo**: Aprender SQL através de jogos interativos
