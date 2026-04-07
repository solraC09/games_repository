from pydantic import BaseModel

class Game(BaseModel):
    nome: str
    plataforma: str
    genero: str
    classificacao: str
    ano_lancamento: int
    preco: float
    multiplayer: bool