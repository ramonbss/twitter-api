FROM python:3.12-alpine
WORKDIR /api_twitter

COPY ./requirements.txt /api_twitter/
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /api_twitter/app
COPY .env /api_twitter
COPY ./tests /api_twitter/tests

EXPOSE 8002

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8002"]