def test_app_is_created(app):
    assert app.name == 'margaret_back.app'


json_mentor_sucess = {
    "name": "Mestre Kame",
    "email": "kame.casadas@ccc.ufcg.edu.br",
    "discord": "kame#3569",
    "state": "NÂO SEI"
}

json_mentor_empty_email = {
    "name": "Jiraya Sensei",
    "email": "",
    "discord": "Jiraya#8596",
    "state": "NÂO SEI"
}

json_mentor_invalid_discord = {
    "name": "Jiraya Sensei",
    "email": "jiraya.casadas@ccc.ufcg.edu.br",
    "discord": "",
    "state": "NÂO SEI"
}


def test_add_mentor_sucess(client):
    response = client.post("/mentor/", json=json_mentor_sucess)
    assert response.status_code == 200
    assert response.get_json() == {
        "name": "MESTRE KAME",
        "email": "kame.casadas@ccc.ufcg.edu.br",
        "discord_id": "kame#3569",
        "state": "NÂO SEI"
    }


def test_add_mentor_used_email(client):
    response = client.post("/mentor/", json=json_mentor_sucess)
    assert response.status_code == 409
    assert response.get_json() == {"message": "Email já em uso"}


def test_add_mentor_invalid_email(client):
    response = client.post('/mentor/', json=json_mentor_empty_email)
    assert response.status_code == 409
    assert response.get_json() == {"message": "Email inválido!"}


def test_add_mentor_invalid_discord(client):
    response = client.post('/mentor/', json=json_mentor_invalid_discord)
    assert response.status_code == 409
    assert response.get_json() == {"message": "Discord ID não pode ser vazio!"}


def test_list_mentors_sucess(client):
    response = client.get("/mentor/")
    assert response.status_code == 200
    print(response.get_json())
    assert response.get_json() == [
        {
            "name": "MESTRE KAME",
            "email": "kame.casadas@ccc.ufcg.edu.br",
            "discord_id": "kame#3569",
            "state": "NÂO SEI"
        }
    ]


def test_remove_mentor_sucess(client):
    response = client.delete("/mentor/",
                             json={"email": "kame.casadas@ccc.ufcg.edu.br"})
    assert response.status_code == 200
    assert response.get_json() == {
        "name": "MESTRE KAME",
        "email": "kame.casadas@ccc.ufcg.edu.br",
        "discord_id": "kame#3569",
        "state": "NÂO SEI"
    }


def test_remove_mentor_nonexistent(client):
    response = client.delete("/mentor/",
                             json={"email": "kame.casadas@ccc.ufcg.edu.br"})
    assert response.status_code == 404
    assert response.get_json() == {"message": "Usuário não inscrito"}


def test_update_mentor_nonexistent(client):
    response = client.patch("/mentor/", json={
        "email": "kame.casadas@ccc.ufcg.edu.br",
        "atribute": "name",
        "value": "Muten Roshi"
    })

    assert response.status_code == 404
    assert response.get_json() == {"message": "Usuário não inscrito"}


def test_update_mentor_nonexistent(client):
    client.post('/mentor/', json=json_mentor_sucess)

    response = client.patch("/mentor/", json={
        "email": "kame.casadas@ccc.ufcg.edu.br",
        "atribute": "name",
        "value": "Muten Roshi"
    })
    assert response.status_code == 200
    assert response.get_json() == {
        "name": "MUTEN ROSHI",
        "email": "kame.casadas@ccc.ufcg.edu.br",
        "discord_id": "kame#3569",
        "state": "NÂO SEI"
    }


def test_search_mentor_sucess_1_result(client):
    response = client.get(
        '/mentor/search/',
        json={
            "atribute": "name",
            "value": "MUTEN ROSHI"})
    assert response.status_code == 200
    assert response.get_json() == [
        {
            "name": "MUTEN ROSHI",
            "email": "kame.casadas@ccc.ufcg.edu.br",
            "discord_id": "kame#3569",
            "state": "NÂO SEI"
        }
    ]
