def test_register_user(client):
    response = client.post("/auth/register",
                           json={
                               "nome": "teste pereira",
                               "email": "emailteste@gmail.com",
                               "senha": "teste123"
                           }
                        )

    assert response.status_code == 201

    data = response.json()

    assert data["menssage"] == "Usuário cadastrado"
    assert data["email"] == "emailteste@gmail.com"


def test_register_email_invalid(client):
    response = client.post("/auth/register",
                           json={
                               "nome": "Teste Pereira",
                               "email": "emailinvalido123",
                               "senha": "teste123"
                           }
                        )

    assert response.status_code == 422

def test_duplicated_email(client, user_teste):
    response = client.post("/auth/register",
                            json={
                                "nome": "Novo Usuario",
                                "email": user_teste.email,
                                "senha": "Teste123"
                            }   
                        )

    assert response.status_code == 409

def test_login_user(client, user_teste):
    response = client.post("/auth/login",
                           json={
                               "email": user_teste.email,
                               "senha": "teste123"
                           }
                        )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_invalid_login(client, user_teste):
    response = client.post("/auth/login",
                           json={
                               "email": "email@gmail.com",
                               "senha": "123Teste"
                           }
                        )

    assert response.status_code == 401

def test_invalid_token(client, invalid_auth_header):
    response = client.get("/auth/me",
                            headers=invalid_auth_header  
                        )

    assert response.status_code == 401