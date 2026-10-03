def test_main_route(client):
    response = client.get("/home")

    assert response.status_code == 200
    assert response.json() == {"menssage": "Api funcionando"}