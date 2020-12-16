import pytest


def test_config_is_loaded(config):
    assert config['DEBUG'] is False


def test_request_returns_404(client):
    assert client.get("/").status_code == 404


def test_request_returns_404(client):
    assert client.get('/').status_code == 404


# def test_api_hello(client):
#     res = client.get('/hello')
#     assert res.json == {'OpenDevUFCG': 'Margaret'}


@pytest.mark.options(debug=False)
def test_dd(app):
    assert not app.debug, 'Check debug mode'


def test_debug_is_false(config):
    assert config['DEBUG'] == False


def test_config_is_production(config):
    assert config['TESTING'] == False
