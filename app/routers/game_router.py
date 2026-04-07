from fastapi import APIRouter
from games_repository.app.schemas.game_schema import Game
from games_repository.app.services.game_service import *

router = APIRouter()

@router.get("/games")
def list_games():
    return get_all_games_service()

@router.post("/games")
def create_game(game: Game):
    return create_game_service(game)

@router.get("/games/{game_id}")
def get_game(game_id: str):
    return get_game_by_id_service(game_id)

@router.put("/games/{game_id}")
def update_game(game_id: str, game: Game):
    return update_game_service(game_id, game)

@router.delete("/games/{game_id}")
def delete_game(game_id: str):
    return delete_game_service(game_id)

@router.get("/games/search/{genero}")
def search_games(genero: str):
    return search_games_service(genero)

@router.get("/games/year/{ano_lancamento}")
def get_year_games(ano_lancamento: int):
    return get_games_year_service(ano_lancamento)