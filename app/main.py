from fastapi import FastAPI
from app.api.routers import router as tuite_router

app = FastAPI()

app.include_router(tuite_router)
