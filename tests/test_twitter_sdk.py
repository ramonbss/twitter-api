import pytest
import requests_mock
from classes.credenciais import Credentials


@pytest.fixture
def credencials_api():
    return {
        "consumer_key": "",
        "consumer_secret": "",
        "access_token": "",
        "access_token_secret": "",
    }


def test_leitura_credenciais_da_api():
    assert Credentials.ACCESS_TOKEN
    assert Credentials.ACCESS_TOKEN_SECRET
    assert Credentials.CONSUMER_KEY
    assert Credentials.CONSUMER_SECRET
