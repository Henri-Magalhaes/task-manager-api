# API de Tarefas

API REST para gerenciamento de tarefas, desenvolvida com Python e FastAPI.

O projeto foi desenvolvido como prática de desenvolvimento Backend, aplicando conceitos de autenticação, banco de dados, organização em camadas e testes automatizados.

## Tecnologias

* Python
* FastAPI
* SQLAlchemy
* PostgreSQL
* Alembic
* Pydantic
* JWT
* Argon2
* Pytest

## Funcionalidades

* Cadastro de usuários
* Login e autenticação com JWT
* Criação de tarefas
* Consulta de tarefas
* Atualização de tarefas
* Exclusão de tarefas
* Controle de status e prioridade
* Validação de dados
* Senhas armazenadas com hash
* Testes automatizados

## Estrutura

O projeto utiliza uma organização em camadas para separar as responsabilidades da aplicação:

```text
app/
├── models/
├── schemas/
├── repositories/
├── services/
├── routers/
├── core/
└── main.py
```

## Como executar

Clone o repositório:

```bash
git clone <URL_DO_REPOSITORIO>
cd API-de-Tarefas
```

Crie e ative o ambiente virtual:

```bash
uv venv
```

Instale as dependências:

```bash
uv sync
```

Configure as variáveis de ambiente necessárias no arquivo `.env`.

Execute as migrações:

```bash
uv run alembic upgrade head
```

Inicie a aplicação:

```bash
uv run uvicorn app.main:app --reload
```

A API estará disponível em:

```text
http://127.0.0.1:8000
```

A documentação interativa pode ser acessada em:

```text
http://127.0.0.1:8000/docs
```

## Testes

Para executar os testes:

```bash
uv run pytest
```

## Objetivo

Este projeto faz parte dos meus estudos em desenvolvimento Backend com Python, com foco em construção de APIs REST, autenticação, bancos de dados e boas práticas de organização de código.

---

**Desenvolvido por [Henri Magalhães]**
