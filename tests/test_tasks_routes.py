from app.schemas.task_schemas import TaskResponse

def test_create_task(client, auth_header):
    response = client.post("/tasks",
                           json={
                               "titulo": "Tarefa Teste",
                               "descriçao": "Descrição-Teste",
                               "status": "ATIVO",
                               "prioridade": "ALTA"
                           },
                           headers=auth_header
                        )

    assert response.status_code == 201

    data = response.json()

    assert data["id"] == 1
    assert data["id_user"] == 1
    assert data["titulo"] == "Tarefa Teste"
    assert data["descriçao"] == "Descrição-Teste"
    assert data["status"] == "ATIVO"
    assert data["prioridade"] == "ALTA"
    

def test_create_invalid_task(client, auth_header):
    response = client.post("/tasks",
                            json={
                                "titulo": "Tarefa Teste",
                                "descriçao": "Descrição-Teste",
                                "status": "INVALID DATA",
                                "prioridade": "INVALID DATA"
                            },
                            headers=auth_header
                        )

    assert response.status_code == 422

def test_not_authorization_route(client):
    response = client.post("/tasks",
                           json={
                               "titulo": "Tarefa Teste",
                               "descriçao": "Descrição-Teste",
                               "status": "ATIVO",
                               "prioridade": "ALTA"
                           }
                        )

    assert response.status_code == 401

    data = response.json()

    assert data["detail"] == "Not authenticated"

def test_search_tasks(client, auth_header, task_test):
    response = client.get("/tasks",
                        headers=auth_header
                        )

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 1

    task = data[0]

    assert task["id"] == task_test.id
    assert task["id_user"] == task_test.id_user
    assert task["titulo"] == task_test.titulo
    assert task["descriçao"] == task_test.descriçao
    assert task["status"] == task_test.status
    assert task["prioridade"] == task_test.prioridade

def test_search_not_found_task(client, auth_header):
    response = client.get("/tasks",
                            headers=auth_header
                        )

    assert response.status_code == 404

def test_search_id_task(client, auth_header, task_test):
    response = client.get(f"/tasks/{task_test.id}",
                            headers=auth_header  
                        )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == task_test.id
    assert data["id_user"] == task_test.id_user
    assert data["titulo"] == task_test.titulo
    assert data["descriçao"] == task_test.descriçao
    assert data["status"] == task_test.status
    assert data["prioridade"] == task_test.prioridade

def test_search_id_task_not_found(client, auth_header):
    response = client.get(f"/tasks/1",
                            headers=auth_header  
                        )

    assert response.status_code == 404

def test_update_task(client, auth_header, task_test):
    response = client.patch(f"/tasks/{task_test.id}",
                            json={
                                "titulo": "Estudar Python",
                                "descriçao": "Devo estudar python até 20Hr",
                                "status": "ATIVO",
                                "prioridade": "ALTA"
                            },
                            headers=auth_header   
                        )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["id_user"] == 1
    assert data["titulo"] == "Estudar Python"
    assert data["descriçao"] == "Devo estudar python até 20Hr"
    assert data["status"] == "ATIVO"
    assert data["prioridade"] == "ALTA"

def test_parcial_update(client, auth_header, task_test):
    response = client.patch(f"/tasks/{task_test.id}",
                                json={
                                    "descriçao": "Nova Descrição",
                                    "status": "CONCLUIDO"
                                },
                                headers=auth_header
                            )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["id_user"] == 1
    assert data["titulo"] == task_test.titulo
    assert data["descriçao"] == "Nova Descrição"
    assert data["status"] == "CONCLUIDO"
    assert data["prioridade"] == task_test.prioridade

def test_update_task_not_found(client, auth_header):
    response = client.patch("/tasks/1",
                                json={
                                    "titulo": "Estudar Python",
                                    "descriçao": "Devo estudar python até 20Hr",
                                    "status": "ATIVO",
                                    "prioridade": "ALTA"
                                },
                                headers=auth_header   
                            )

    assert response.status_code == 404

def test_delete_task(client, auth_header, task_test):
    response = client.delete(f"/tasks/{task_test.id}",
                                headers=auth_header 
                            )

    assert response.status_code == 204

def test_delete_task_not_found(client, auth_header):
    response = client.delete("/tasks/1",
                                headers=auth_header
                            )

    assert response.status_code == 404