from games_repository.app.repositories.game_repository import *

def format_game(game):
    game["_id"] = str(game["_id"])
    return game

def create_game_service(game):
    result = create_game(game.model_dump())
    return {
        "message": "Game successfully created",
        "id": str(result.inserted_id)
    }

def get_all_games_service():
    games = get_all_games()
    return [format_game(game) for game in games]

def get_game_by_id_service(game_id):
    try:
        game = get_game_by_id(game_id)
    except:
        return {"error": "Invalid ID format"}
    if not game:
        return {"error": "Game not found"}
    return format_game(game)

def update_game_service(game_id, game):
    try:
        result = update_game(game_id, game.model_dump())
    except:
        return {"error": "Invalid ID format"}
    if result.matched_count == 0:
        return {"error": "Game not found"}
    return {"message": "Game successfully updated"}

def delete_game_service(game_id):
    try:
        result = delete_game(game_id)
    except:
        return {"error": "Invalid ID format"}
    if result.deleted_count == 0:
        return {"error": "Game not found"}
    return {"message": "Game successfully deleted"}

def search_games_service(genero):
    games = search_games_by_genero(genero)
    return [format_game(game) for game in games]

def get_games_year_service(ano_lancamento):
    games = get_games_year(ano_lancamento)
    return [format_game(game) for game in games]