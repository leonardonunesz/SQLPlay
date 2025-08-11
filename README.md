# SQLPlay

## Sobre o Projeto

SQLPlay é uma aplicação web interativa desenvolvida para ensinar SQL através de mini-jogos educativos. O projeto combina conceitos de programação com gamificação para criar uma experiência de aprendizado envolvente e prática.

## Objetivo

O objetivo principal é auxiliar desenvolvedores e estudantes a aprenderem SQL de forma prática e divertida, permitindo que pratiquem comandos SQL reais em um ambiente controlado e educativo.

## Tecnologias Utilizadas

- **Backend**: Django (Python)
- **Frontend**: HTML5, CSS3, JavaScript ES6+
- **Banco de Dados**: SQLite (desenvolvimento) / MySQL (produção)
- **Framework CSS**: CSS Grid, Flexbox, Media Queries
- **Ícones**: Font Awesome 6.0
- **Fontes**: Google Fonts (Inter)

## Funcionalidades Implementadas

### Jogo da Velha SQL
- **Modo Multijogador Local**: Dois jogadores alternando turnos
- **Modo Single Player**: Jogador contra computador com IA aleatória
- **Sistema SQL**: Comandos INSERT INTO e UPDATE para fazer jogadas
- **Validação**: Verificação de sintaxe SQL e regras do jogo
- **Interface Responsiva**: Adaptável para desktop, tablet e mobile

## Como Funciona

1. **Seleção de Modo**: O usuário escolhe entre multijogador local ou contra computador
2. **Execução SQL**: Em vez de clicar nas células, o jogador digita comandos SQL
3. **Validação**: O sistema valida a sintaxe e aplica as regras do jogo
4. **Feedback**: Mensagens de erro ou sucesso são exibidas
5. **Alternância**: Os jogadores alternam automaticamente após cada jogada válida

## Estrutura do Projeto

O projeto segue uma arquitetura modular e organizada:

- **`core/`**: Aplicação principal com página inicial
- **`jogo_da_velha/`**: Aplicação específica do jogo da velha
- **`static/`**: Arquivos estáticos organizados por tipo (CSS, JS, imagens)
- **`templates/`**: Templates HTML organizados por aplicação
- **`sqlplay/`**: Configurações principais do projeto Django

## Instalação e Configuração

### Pré-requisitos
- Python 3.8+
- pip
- Virtual environment

### Passos para Instalação

1. **Clone o repositório**
   ```bash
   git clone https://github.com/leonardonunesz/SQLPlay.git
   cd SQLPlay
   ```

2. **Crie e ative o ambiente virtual**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   # ou
   venv\Scripts\activate  # Windows
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute as migrações**
   ```bash
   python manage.py migrate
   ```

5. **Inicie o servidor**
   ```bash
   python manage.py runserver
   ```

6. **Acesse a aplicação**
   - Abra o navegador em `http://localhost:8000`

## Comandos SQL Aceitos

### Estrutura do Banco
O tabuleiro é representado por uma tabela com as colunas:
- `linha`: posição vertical (0, 1, 2)
- `coluna`: posição horizontal (0, 1, 2)
- `valor`: 'X' ou 'O'

### Exemplos de Comandos
```sql
-- Inserir uma jogada
INSERT INTO tabuleiro (linha, coluna, valor) VALUES (0, 0, 'X');

-- Atualizar uma posição
UPDATE tabuleiro SET valor = 'O' WHERE linha = 1 AND coluna = 1;
```

## Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Roadmap

- [ ] Palavra Cruzada SQL
- [ ] Quebra-cabeça de SELECTs
- [ ] Sudoku SQL
- [ ] Sistema de pontuação
- [ ] Múltiplos níveis de dificuldade
- [ ] Modo multiplayer online

## Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## Contato

- **Desenvolvedor**: [@leonardonunesz](https://github.com/leonardonunesz)
- **Projeto**: [SQLPlay](https://github.com/leonardonunesz/SQLPlay)

## Agradecimentos

Agradecimentos especiais à comunidade Django e Python por fornecer as ferramentas necessárias para tornar este projeto possível.

---

**Desenvolvido com ❤️ por [@leonardonunesz](https://github.com/leonardonunesz)**
