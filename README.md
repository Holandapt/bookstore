# Django Bookstore API

Projeto desenvolvido com **Django**, utilizando **Poetry** para a gestão de dependências e **Pytest** juntamente com **Factory Boy** para a execução de testes automatizados.

## Pré-requisitos:

Certifique-se de ter instalado no seu sistema:  
- Python (versão 3.10 ou superior recomendada)
- Poetry (gestor de dependências)

## Clone o repositõrio:

```bash
git clone https://github.com/Holandapt/bookstore
cd bookstore
```
# O Poetry irá criar e configurar um ambiente virtual automaticamente com base nos ficheiros.

## Execute as migrações da base de dados:

```bash
poetry run python manage.py migrate
```

# Podemos rodar o projeto com:

```bash
poetry run python manage.py runserver
```

# Podemos rodar os testes com:

```bash
poetry run pytest
```