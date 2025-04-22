# SQLPlay – Aprendendo SQL

Um aplicativo web interativo com mini-jogos educativos onde você joga utilizando **comandos SQL**!  
Desenvolvido com **Flask (Python)** no backend e **MySQL** como banco de dados, o projeto tem o objetivo de ensinar SQL de forma divertida, prática e criativa.

---

## Objetivo do Projeto

> Aprender e praticar SQL de maneira interativa, utilizando joguinhos onde a manipulação e consulta de dados são feitas através de comandos SQL reais.

---

## Objetivos Didáticos

- Praticar comandos SQL de maneira divertida.
- Treinar estrutura de banco de dados relacional.
- Aprender como conectar Python a bancos reais (MySQL).
- Desenvolver raciocínio lógico com validações e manipulações de dados.
- Criar um sistema completo: **frontend + backend + banco de dados**.

---

## Tecnologias Utilizadas

### Backend

- [Python 3](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [MySQL](https://www.mysql.com/)
- [mysql-connector-python](https://pypi.org/project/mysql-connector-python/) ou [PyMySQL](https://pypi.org/project/PyMySQL/)

### Frontend

- HTML + Jinja2 (template engine do Flask)
- CSS

---

## Mini-jogos Planejados

- Jogo da Velha
- Palavra Cruzada SQL
- Quebra-cabeça de SELECTs
- Sudoku SQL

---

## Modelagem de Banco (exemplo: Jogo da Velha)

**Banco:** `sqlplay`

### Tabela: `tabuleiro`

| id  | linha | coluna | valor |
| --- | ----- | ------ | ----- |
| 1   | 1     | 1      | 'X'   |

### Tabela: `historico_partidas`

| id  | jogador | resultado | data       |
| --- | ------- | --------- | ---------- |
| 1   | Lucas   | Vitória   | 2025-04-22 |

---

## Fluxo do Jogo

1. Acesso à página inicial: escolha do mini-jogo.
2. Flask carrega o estado atual do jogo do MySQL.
3. Usuário digita um comando SQL (ex: `UPDATE`, `SELECT`, etc).
4. O Flask executa o comando no banco.
5. Validação é feita com lógica em Python (ex: comando permitido? jogada válida?).
6. Feedback mostrado (acertou, errou, venceu, etc.).
7. Fim de jogo → histórico salvo no banco → opção de jogar novamente.

---

## 💡 Futuras Melhorias

- Sistema de login e pontuação
- Ranking de jogadores
- Novos jogos com níveis de dificuldade
- Tutoriais interativos por jogo
- Validação de SQL mais robusta (evitar injeção, etc)

---

## 🤝 Contribuições

Esse é um projeto pessoal de aprendizado.  
Sinta-se livre para sugerir melhorias ou ideias de novos mini-jogos baseados em SQL!
