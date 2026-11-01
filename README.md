# Sistema de Biblioteca

O projeto foi desenvolvido para a disciplina de Programação para Servidores Web (PSI).

## Tema escolhido

**Sistema de Biblioteca**: É uma aplicação web para cadastrar autores, livros e leitores,
além de registrar e remover empréstimos de livros.

## Integrantes do grupo e responsabilidades

## Nome do Jhaelson: Modelagem do banco, models e relacionamentos 
## Nome do Jeseane: Controllers, rotas e CRUD
## Nome do Júlio César: Templates, seed e documentação

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



