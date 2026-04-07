from database import games_collection
from bson import ObjectId

def create_game(game_dict):
    return games_collection.insert_one(game_dict)

def get_all_games():
    return list(games_collection.find())

def get_game_by_id(game_id):
    return games_collection.find_one({"_id": ObjectId(game_id)})

def update_game(game_id, game_dict):
    return games_collection.update_one(
        {"_id": ObjectId(game_id)},
        {"$set": game_dict}
    )

def delete_game(game_id):
    return games_collection.delete_one(
        {"_id": ObjectId(game_id)}
    )

def search_games_by_genero(genero):
    return list(games_collection.find({"genero": genero}))

def get_games_year(ano_lancamento):
    return list(games_collection.find({"ano_lancamento": ano_lancamento}))
