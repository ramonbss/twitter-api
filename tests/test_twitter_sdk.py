import pytest
import requests_mock
from app.services.credenciais import TwitterCredentials
from app.services.twitter import Twitter


@pytest.fixture
def credenciais_api():
    return {
        "consumer_key": "",
        "consumer_secret": "",
        "access_token": "",
        "access_token_secret": "",
    }


@pytest.fixture
def twitter(credenciais_api):
    return Twitter(**credenciais_api)


@pytest.fixture
def texto_do_tuite():
    return "Novo tuite"


@pytest.fixture
def resposta_tuite_criado(texto_do_tuite):
    return {
        "data": {
            "edit_history_tweet_ids": ["1234567890"],
            "id": "1234567890",
            "text": texto_do_tuite,
        }
    }


@pytest.fixture
def resposta_falha_criar_tuite():
    return {
        "title": "Unauthorized",
        "type": "about:blank",
        "status": 401,
        "detail": "Unauthorized",
    }


def test_leitura_credenciais_da_api():
    assert TwitterCredentials.ACCESS_TOKEN
    assert TwitterCredentials.ACCESS_TOKEN_SECRET
    assert TwitterCredentials.CONSUMER_KEY
    assert TwitterCredentials.CONSUMER_SECRET


def test_tuite_criado_com_sucesso(twitter, resposta_tuite_criado, texto_do_tuite):
    with requests_mock.Mocker() as mocker:
        mocker.post(twitter.API_ENDPOINT, json=resposta_tuite_criado, status_code=201)
        resposta = twitter.post_tuite(texto_do_tuite)

        assert resposta["data"]["text"] == texto_do_tuite


def test_falha_criar_tuite(twitter, texto_do_tuite, resposta_falha_criar_tuite):
    with requests_mock.Mocker() as mocker:
        mocker.post(
            twitter.API_ENDPOINT, json=resposta_falha_criar_tuite, status_code=401
        )
        resposta = twitter.post_tuite(texto_do_tuite)

        assert resposta["status"] >= 400
