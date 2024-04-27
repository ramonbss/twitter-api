from fastapi import APIRouter, HTTPException, status, Body
from app.services.twitter import Twitter
from app.services.credenciais import TwitterCredentials

router = APIRouter()

twitter = Twitter(
    TwitterCredentials.CONSUMER_KEY,
    TwitterCredentials.CONSUMER_SECRET,
    TwitterCredentials.ACCESS_TOKEN,
    TwitterCredentials.ACCESS_TOKEN_SECRET,
)


@router.post("/tuitar_temperatura", status_code=status.HTTP_201_CREATED)
def tuitar_temperatura(texto: str = Body(embed=True)):
    try:
        resposta = twitter.post_tuite(texto)
        if "data" not in resposta:
            raise Exception(resposta)
        else:
            return "Tuite criado com sucesso!"

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
