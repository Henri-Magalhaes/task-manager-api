import pytest

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool
from datetime import timedelta

from app.main import app
from app.core.database import Base
from app.dependencies import get_session
from app.core.security import hash_password, create_token
from app.models import User, Task

TEST_DATABASE_URL = "sqlite://"

@pytest.fixture
def test_engine():
    engine = create_engine(
        TEST_DATABASE_URL,
        connect_args={
            "check_same_thread": False
        },
        poolclass=StaticPool,
    )

    Base.metadata.create_all(bind=engine)

    yield engine

    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def db_session(test_engine):

    with Session(test_engine) as db:
        yield db

@pytest.fixture
def client(db_session):

    def get_test_session():
        yield db_session

    app.dependency_overrides[get_session] = get_test_session

    with TestClient(app) as client:
        yield client

    app.dependency_overrides.clear()

@pytest.fixture
def user_teste(db_session):
    user = User(
        nome="Teste Pereira",
        email="emailteste@gmail.com",
        hash_senha=hash_password("teste123")
    )

    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)

    return user

@pytest.fixture
def token(client, user_teste):
    response = client.post("/auth/login",
                           json={
                               "email": user_teste.email,
                                "senha": "teste123"
                           }
                        )

    return response.json()["access_token"]

@pytest.fixture
def auth_header(token):
    return {
        "Authorization": f"Bearer {token}"
    }

@pytest.fixture
def invalid_auth_header():
    token = create_token(1, "invalid", timedelta(days=7))

    return {
        "Authorization": f"Bearer {token}"
    }

@pytest.fixture
def task_test(db_session, user_teste):
    task = Task(
        id_user=user_teste.id,
        titulo="Tarefa Teste",
        descriçao="Descricao Teste",
        status="ATIVO",
        prioridade="MEDIA"
    )

    db_session.add(task)
    db_session.commit()
    db_session.refresh(task)

    return task