# Twitter FastAPI

## Visão Geral

Este projeto é uma aplicação FastAPI que integra a API do Twitter para fazer envios de tuites de forma automatizada.

## Começando

### Instalação

Para começar a usar este projeto, siga os passos abaixo:

1. Clone o repositório do projeto:
   ```
    git clone https://github.com/ramonbss/twitter-api
    ```
1. Navegue até o diretório do projeto:
   ```
    cd twitter-api
    ```
1. Instale as dependências necessárias:
    ```
    pip install -r requirements.txt
    ```

### Executando a Aplicação
Para iniciar o servidor FastAPI, execute o seguinte comando:
   ```
   uvicorn app.main:app
   ```

A porta padrão será a 8000. A mesma pode ser modificada através do parametro `--port`.

## Configurações

### Obter Chaves de API
Acesse [Twitter Developers ](https://developer.twitter.com/)
 e crie uma conta para obter sua chave de API.

### Configuração Local
Antes de iniciar a aplicação, é necessário configurar a credencial para a API do Twitter. Essas credenciais devem ser armazenadas de forma segura e podem ser configuradas como variáveis de ambiente, onde serão lidas no módulo **app.services.credenciais**.


### Utilizando a API
#### Fazer tuite
Envie uma requisição HTTP POST para o endpoint **/tuitar_temperatura** incluindo o nome da cidade como parâmetro. Por exemplo (utilizando a biblioteca httpie):
```
http -v localhost:8000/tuitar_temperatura texto="Meu tuite aqui"
```
