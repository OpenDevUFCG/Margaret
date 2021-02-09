def test_app_is_created(app):
    assert app.name == 'margaret_back.app'


json_sub = {
    "name": "Josef Stalin",
    "email": "josef.stalin@ccc.ufcg.edu.br",
    "discord_id": "Stalin#1511",
    "period": "2020.1",
    "minority_group": ""}
json_sub_2 = {
    "name": "Fidel Castro",
    "email": "fidel.castro@ccc.ufcg.edu.br",
    "discord_id": "Castro#1511",
    "period": "2020.1",
    "minority_group": ""}
json_sub_miss = {
    "name": "Josef Stalin",
    "discord_id": "",
    "email": "josef.stalin@ccc.ufcg.edu.br",
    "period": "2020.1",
    "minority_group": ""}


def test_add_subscribed_first_status_code(client):
    assert client.post("/subscribed/", json=json_sub).status_code == 200


def test_add_subscribed_repeated_status_code(client):
    assert client.post("/subscribed/", json=json_sub).status_code == 400


def test_add_subscribed_new_json(client):
    assert client.post(
        "/subscribed/",
        json=json_sub_2).get_json() == {
        "_discord_id": "Castro#1511",
        "_email": "fidel.castro@ccc.ufcg.edu.br",
        "_name": "FIDEL CASTRO",
        "_period": "2020.1",
        "minority_group": ""}


def test_add_subscribed_miss_attribute_status_code(client):
    assert client.post("/subscribed/", json=json_sub_miss).status_code == 400


def test_list_subscribed_status_code(client):
    assert client.get("/subscribed/").status_code == 200


def test_list_subscribed(client):
    assert client.get("/subscribed/").get_json() == {
        "1": {
            "_discord_id": "Stalin#1511",
            "_email": "josef.stalin@ccc.ufcg.edu.br",
            "_name": "JOSEF STALIN",
            "_period": "2020.1",
            "minority_group": ""
        },
        "2": {
            "_discord_id": "Castro#1511",
            "_email": "fidel.castro@ccc.ufcg.edu.br",
            "_name": "FIDEL CASTRO",
            "_period": "2020.1",
            "minority_group": ""
        }
    }


def test_remove_subscribed_first(client):
    assert client.delete(
        "/subscribed/",
        json={
            "email_user": "josef.stalin@ccc.ufcg.edu.br"}).status_code == 200


def test_remove_subscribed_new(client):
    assert client.delete(
        "/subscribed/",
        json={
            "email_user": "fidel.castro@ccc.ufcg.edu.br"}).get_json() == {
        "_discord_id": "Castro#1511",
        "_email": "fidel.castro@ccc.ufcg.edu.br",
        "_name": "FIDEL CASTRO",
        "_period": "2020.1",
        "minority_group": ""}


def test_remove_subscribed_again(client):
    assert client.delete(
        "/subscribed/",
        json={
            "email_user": "fidel.castro@ccc.ufcg.edu.br"}).status_code == 404


def test_get_subscribed_status_code(client):
    test_add_subscribed_first_status_code(client)
    assert client.get("/subscribed/josef.stalin").status_code == 200


def test_get_subscribed_status_json(client):
    assert client.get("/subscribed/josef.stalin").get_json() == {
        "_name": "JOSEF STALIN",
        "_email": "josef.stalin@ccc.ufcg.edu.br",
        "_discord_id": "Stalin#1511",
        "_period": "2020.1",
        "minority_group": ""}


def test_get_subscribed_status_code_not_found(client):
    assert client.get("/subscribed/raul.castro").status_code == 404


json_sub_modify = {"attribute": "period", "new_attribute": "2020.2"}
json_sub_modify2 = {"attribute": "", "new_attribute": "2020.2"}
json_sub_modify_email = {"attribute": "email", "new_attribute": "2020.2"}
json_sub_modify_discord = {
    "attribute": "discord_id", "new_attribute": "Stalin#1313"}
json_sub_modify_discord_wrong = {
    "attribute": "discord_id", "new_attribute": "Stalin"}


def test_modify_subscribed_status_code(client):
    assert client.post("/subscribed/josef.stalin",
                       json=json_sub_modify).status_code == 200


def test_modify_subscribed_status_code_wrong_attribute(client):
    assert client.post("/subscribed/josef.stalin",
                       json=json_sub_modify2).status_code == 400


def test_modify_subscribed_status_code_modify_email(client):
    assert client.post("/subscribed/josef.stalin",
                       json=json_sub_modify_email).status_code == 400


def test_modify_subscribed_status_code_wrong_discord(client):
    assert client.post("/subscribed/josef.stalin",
                       json=json_sub_modify_discord_wrong).status_code == 400


def test_modify_subscribed_status_code_modify_discord(client):
    assert client.post(
        "/subscribed/josef.stalin",
        json=json_sub_modify_discord).get_json() == {
        "_name": "JOSEF STALIN",
        "_email": "josef.stalin@ccc.ufcg.edu.br",
        "_discord_id": "Stalin#1313",
        "_period": "2020.2",
        "minority_group": ""}


json_search_sub = {"attribute": "period", "value_attribute": "2020.1"}
json_search_sub2 = {"attribute": "discord_id",
                    "value_attribute": "Stalin#1313"}
json_search_sub3 = {"attribute": "name", "value_attribute": "FIDEL CASTRO"}
json_search_sub4 = {"attribute": "email",
                    "value_attribute": "josef.stalin@ccc.ufcg.edu.br"}
json_search_sub5 = {"attribute": "email",
                    "value_attribute": "raul.castro@ccc.ufcg.edu.br"}


def test_search_sub_by_period_status_code(client):
    test_add_subscribed_new_json(client)
    assert client.get("/subscribed/search",
                      json=json_search_sub).status_code == 200


def test_search_sub_by_period_json(client):
    assert client.get("/subscribed/search",
                      json=json_search_sub).get_json() == {"1": {
                          "_discord_id": "Castro#1511",
                          "_email": "fidel.castro@ccc.ufcg.edu.br",
                          "_name": "FIDEL CASTRO", "_period": "2020.1",
                          "minority_group": ""}}


def test_search_sub_by_discord_status_code(client):
    assert client.get("/subscribed/search",
                      json=json_search_sub2).status_code == 200


def test_search_sub_by_discord_json(client):
    assert client.get("/subscribed/search",
                      json=json_search_sub2).get_json() == {"1": {
                          "_name": "JOSEF STALIN",
                          "_email": "josef.stalin@ccc.ufcg.edu.br",
                          "_discord_id": "Stalin#1313",
                          "_period": "2020.2",
                          "minority_group": ""}}


def test_search_sub_by_name_status_code(client):
    assert client.get("/subscribed/search",
                      json=json_search_sub3).status_code == 200


def test_search_sub_by_name_json(client):
    assert client.get("/subscribed/search",
                      json=json_search_sub).get_json() == {"1": {
                          "_discord_id": "Castro#1511",
                          "_email": "fidel.castro@ccc.ufcg.edu.br",
                          "_name": "FIDEL CASTRO",
                          "_period": "2020.1",
                          "minority_group": ""}}


def test_search_sub_by_email_status_code(client):
    assert client.get("/subscribed/search",
                      json=json_search_sub4).status_code == 200


def test_search_sub_by_email_json(client):
    assert client.get("/subscribed/search",
                      json=json_search_sub4).get_json() == {"1": {
                          "_name": "JOSEF STALIN",
                          "_email": "josef.stalin@ccc.ufcg.edu.br",
                          "_discord_id": "Stalin#1313",
                          "_period": "2020.2",
                          "minority_group": ""}}


def test_search_sub_miss_attribute(client):
    assert client.get(
        "/subscribed/search",
        json={
            "attribute": "",
            "value_attribute": "Josef Stalin"}) == 400


def test_search_sub_empty(client):
    assert client.get("/subscribed/search",
                      json=json_search_sub5).get_json() == {}
