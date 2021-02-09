import pytest
from margaret_back.app import create_app


@pytest.fixture(scope='module')
def app():
    return create_app()
