from fastapi import FastAPI
from games_repository.app.routers.game_router import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {"Message": "P1 Beck-end e Banco de Dados"}