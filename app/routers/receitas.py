from fastapi import APIRouter, HTTPException
from pymongo.collection import Collection
from app.utils.database import Database
from app.utils.receitas import get_receitas, get_receita_by_id, add_receita, update_receita, delete_receita
from app.models.receita import Receita
from bson import ObjectId

router = APIRouter()


@router.get("/")
def welcome():
    return 'Bem vindo à API de Receitas!'

# Trazer todas as receitas(configurei para trazer apenas 10 por enquanto)
@router.get("/receitas/", response_model=list[Receita])
def listar_receitas():
    return get_receitas(Database.get_collection("receitas"))

# Trazer receita pelo id
@router.get("/receitas/{receita_id}", response_model=Receita)
def obter_receita(receita_id: str):
    receita = get_receita_by_id(Database.get_collection("receitas"), ObjectId(receita_id))
    if receita:
        return receita
    raise HTTPException(status_code=404, detail="Receita não encontrada")

# Adicionar uma receita nova
@router.post("/receitas/", response_model=Receita)
def adicionar_receita(receita: Receita):
    add_receita(Database.get_collection("receitas"), receita)
    return receita

# Editar uma receita existente pelo id
@router.put("/receitas/{receita_id}", response_model=Receita)
def atualizar_receita(receita_id: str, receita: Receita):
    update_receita(Database.get_collection("receitas"), ObjectId(receita_id), receita)
    return receita

# Apagar uma receita pelo id
@router.delete("/receitas/{receita_id}", response_model=dict)
def excluir_receita(receita_id: str):
    delete_receita(Database.get_collection("receitas"), ObjectId(receita_id))
    return {"message": "Receita excluída"}
