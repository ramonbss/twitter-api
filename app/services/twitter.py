from requests_oauthlib import OAuth1Session
from dataclasses import dataclass


class Twitter:
    API_ENDPOINT = "https://api.twitter.com/2/tweets"

    def __init__(
        self,
        consumer_key: str,
        consumer_secret: str,
        access_token: str,
        access_token_secret: str,
    ) -> None:
        self._twitter = OAuth1Session(
            consumer_key, consumer_secret, access_token, access_token_secret
        )
        pass

    def post_tuite(self, texto: str):
        payload = {"text": texto}
        response = self._twitter.post(self.API_ENDPOINT, json=payload)

        if response.status_code == 201:
            print("Tuite feito com sucesso!")
        else:
            print(f"Falha ao postar tuite: {response.status_code} - {response.text}")
        return response.json().get("data")
