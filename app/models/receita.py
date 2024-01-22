from typing import List
from bson import ObjectId
from pydantic import BaseModel

# Podem ter diversas secoes por isso declaro como outra classe (que sera introduzida dentro da class principal)
class Secao(BaseModel):
    nome: str
    conteudo: List[str]

# Receita sendo a class principal tem id e nome, e apos recebe da classe secao(pois pode ser multiplas. Exemplo: 'Ingredientes', 'Modo de Preparo', 'Comentarios' e etc...)
class Receita(BaseModel):
    _id: ObjectId
    nome: str
    secao: List[Secao]
