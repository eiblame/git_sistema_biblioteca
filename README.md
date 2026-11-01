# Sistema de Biblioteca

O projeto foi desenvolvido para a disciplina de Programação para Servidores Web (PSI).

## Tema escolhido

**Sistema de Biblioteca**: É uma aplicação web para cadastrar autores, livros e leitores,
além de registrar e remover empréstimos de livros.

## Integrantes do grupo e responsabilidades

## Nome do Jhaelson: Modelagem do banco, models e relacionamentos 
## Nome do Jeseane: Controllers, rotas e CRUD
## Nome do Júlio César: Templates, seed e documentação

## Descrição do sistema

O sistema permite:

- Cadastrar, listar, editar e excluir autores, livros e leitores;
- Registrar um empréstimo escolhendo um leitor e um livro;
- Remover um empréstimo sem excluir o leitor nem o livro;
- Ver os livros de cada autor;

## Entidades do sistema

### Autor

Representa o autor dos livros.

### Livro

Representa um livro cadastrado no sistema.

### Leitor

Representa uma pessoa que pode pegar livros emprestados.

### Empréstimo

Representa o vínculo entre um leitor e um livro.

A chave primária da tabela é composta por `leitor_id` e `livro_id`.

## Relacionamento 1:N (Autor e Livro)

Um autor pode possuir vários livros, mas cada livro pertence a um único autor.

## Relacionamento N:N (Leitor e Livro)

Um leitor pode pegar vários livros emprestados, e um mesmo livro pode ser emprestado
para vários leitores em momentos diferentes.


## Estrutura do projeto

```text
sistema_biblioteca/
├── app.py                  # Cria o Flask, configura o SQLite e registra os controllers
├── main.py                 # Forma alternativa de iniciar o sistema
├── database.py             # Cria o objeto db do SQLAlchemy
├── models/
│   ├── __init__.py
│   ├── autor.py            # Model Autor
│   ├── livro.py            # Model Livro
│   ├── leitor.py           # Model Leitor
│   └── emprestimo.py       # Tabela intermediária de empréstimos
├── controllers/
│   ├── __init__.py
│   ├── principal.py        # Página inicial
│   ├── autores.py          # Rotas de autores
│   ├── livros.py           # Rotas de livros
│   ├── leitores.py         # Rotas de leitores
│   └── emprestimos.py      # Rotas de empréstimos
├── templates/
│   ├── base.html           # Página base com menu e mensagens
│   ├── index.html          # Página inicial
│   ├── autores.html
│   ├── autor_form.html
│   ├── autor_detalhe.html
│   ├── livros.html
│   ├── livro_form.html
│   ├── livro_detalhe.html
│   ├── leitores.html
│   ├── leitor_form.html
│   ├── leitor_detalhe.html
│   ├── emprestimos.html
│   └── emprestimo_form.html
├── seed.py                 # Dados de exemplo
├── requirements.txt
├── DIARIO.md
└── README.md
```

## Tecnologias utilizadas

- Python 3
- Flask
- Flask-SQLAlchemy
- SQLAlchemy
- SQLite
- HTML

## Declaração de autoria
Declaração de autoria:

Declaramos que desenvolvi este projeto compreendendo o código entregue e que sou capaz de explicar e modificar suas partes principais.

- [ ] Não utilizei IA generativa.
- [X] Utilizei IA generativa e descrevo abaixo onde e como foi utilizada.
   
   Para auxiliar na construção deste README.md e em algumas dificuldades de entendimento encontradas 



