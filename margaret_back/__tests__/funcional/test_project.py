#  def test_app_is_created(app):
#     assert app.name == 'margaret_back.app'


json_proj = {
    "name": "margaret",
    "description": "essa é a descrição do projeto",
    "base_text": "texto base massa",
    "mentor_name": "augusto",
    "mentor_email": "augusto.araujo@ccc.ufcg.edu.br",
    "discord_id": "Huandrey#6906",
    "organization": "OpenDevUFCG",
    "aux_name": "ricardo",
    "aux_email": "ricardo.mota@ccc.ufcg.edu.br",
    "aux_discord_id": "Huandrey#6906",
    "aux_organization": "Google",
    "areas": ["front"]
    }

json_proj_2 = {
    "name": "margaret",
    "description": "essa é a descrição do projeto",
    "base_text": "texto base massa",
    "mentor_name": "augusto",
    "mentor_email": "augusto.araujo@ccc.ufcg.edu.br",
    "discord_id": "Huandrey#6906",
}

json_proj_3 = {
    "name": "Laguinho",
    "description": "essa é a descrição do projeto",
    "base_text": "texto base massa",
    "mentor_name": "Joao",
    "mentor_email": "joao.araujo@ccc.ufcg.edu.br",
    "discord_id": "Joao#6906",
    "organization": "OpenDevUFCG",
   	"aux_name": "ricardo",
    "aux_email": "ricardo.pereira@ccc.ufcg.edu.br",
    "aux_discord_id": "Ricardo#6906",
    "aux_organization": "OpenDevUFCG",
    "areas": ["front"]
}


def test_add_project_first_status_code(client):
    assert client.post("/project/", json=json_proj_3).status_code == 200

def test_list_project_status_code(client):
    assert client.get("/subscribed/").status_code == 200

def test_return_list_project(client): 
    assert client.get("/project/").get_json() == {
    "1": {
        "_areas": [
        "front"
        ],
        "_state": "Em Análise",
        "aux_mentor": {
        "_discord_id": "Ricardo#6906",
        "_email": "ricardo.pereira@ccc.ufcg.edu.br",
        "_name": "RICARDO",
        "state": "OpenDevUFCG"
        },
        "base_text": "texto base massa",
        "description": "essa é a descrição do projeto",
        "mentor": {
        "_discord_id": "Joao#6906",
        "_email": "joao.araujo@ccc.ufcg.edu.br",
        "_name": "JOAO",
        "state": "OpenDevUFCG"
        },
        "name": "Laguinho",
        "subscribers": {}
    }
}

def test_add_project_repeated_status_code(client):
    assert client.post("/project/", json=json_proj).status_code == 200

def test_add_project_miss_attribute_status_code(client):
    assert client.post("/project/", json=json_proj_2).status_code == 400


json_proj_name = {"attribute": "name", "new_value": "RoadMap"}
json_proj_modify_base_text = {"attribute": "base_text", "new_value": "2020.2"}

# Attribute error
json_proj_modify_error = {"attribute": "inscritos", "new_value": "joaozinho"}

def test_modify_project_base_text_status_code(client):
    client.put("/project/1", json=json_proj_modify_base_text).status_code == 200

def test_modify_project(client):
    assert client.put("/project/1", json=json_proj_name).get_json() == {
        "_areas": [
            "front"
        ],
        "_state": "Em Análise",
        "aux_mentor": {
            "_discord_id": "Ricardo#6906",
            "_email": "ricardo.pereira@ccc.ufcg.edu.br",
            "_name": "RICARDO",
            "state": "OpenDevUFCG"
        },
        "base_text": "texto base massa",
        "description": "essa é a descrição do projeto",
        "mentor": {
            "_discord_id": "Joao#6906",
            "_email": "joao.araujo@ccc.ufcg.edu.br",
            "_name": "JOAO",
            "state": "OpenDevUFCG"
        },
        "name": "RoadMap",
        "subscribers": {}
}

def test_update_attribute_not_exit(client):
    assert client.put("/project/1", json=json_proj_modify_error).status_code == 400

def test_remove_project(client):
    assert client.post("/project/", json=json_proj) == client.delete("/project/1").status_code == 200

def test_delete_project_again(client):
    assert client.delete("/project/1").status_code == 400

def test_delete_project_id_error(client):
    um_id_inexistente = 232345234
    assert client.delete("/project/23452").status_code == 400
