from fastapi import APIRouter, HTTPException, status, Query
from fastapi_pagination import Page, add_pagination, paginate
from pymongo.collection import Collection
from app.infra.database import Database
from app.repository.receitas import *
from app.models.receita import Receita, Secao
from bson import ObjectId
from typing import List

router = APIRouter()

# Deixando como Default 
Page = Page.with_custom_options(
    size=Query(100, ge=1, le=500),
)

@router.get("/")
async def welcome():
    return 'Bem vindo ao DeliciAPI!'

# Buscar todas as receitas
@router.get("/receitas/", response_model=Page[Receita])
async def listar_receitas():
    return paginate(await get_receitas(Database.get_collection("receitas")))

# Buscar receita pelo id
@router.get("/receitas/{receita_id}", response_model=Receita)
async def obter_receita(receita_id: str):
    receita = await get_receita_by_id(Database.get_collection("receitas"), ObjectId(receita_id))
    if receita:
        return receita
    raise HTTPException(status_code=404, detail="Receita não encontrada")

# Adicionar uma receita nova
@router.post("/receitas/")
async def adicionar_receita(receita: Receita):
    response = await add_receita(Database.get_collection("receitas"), receita)
    if response:
        return {"message": "Receita adicionada com sucesso", "status_code": status.HTTP_200_OK}


# Editar uma receita existente pelo id
@router.put("/receitas/{receita_id}")
async def atualizar_receita(receita_id: str, receita: Receita):
    response =  await update_receita(Database.get_collection("receitas"), ObjectId(receita_id), receita)
    if response:
        return {"message": "Receita atualizada com sucesso", "status_code": status.HTTP_200_OK}


# Apagar uma receita pelo id
@router.delete("/receitas/{receita_id}", response_model=dict)
async def excluir_receita(receita_id: str):
    response = await delete_receita(Database.get_collection("receitas"), ObjectId(receita_id))
    if response:
        return {"message": "Receita excluida com sucesso", "status_code": status.HTTP_200_OK}


# Buscar receitas que contenham algum dos ingredientes
@router.get("/receitas/one_ingrediente/{ingredientes}", response_model=Page[Receita])
async def busca_por_ingrediente(ingredientes: str):
    receitas = await get_receita_by_ingrediente(Database.get_collection("receitas"), ingredientes.split(",") )
    if receitas:
        return paginate(receitas)
    raise HTTPException(status_code=404, detail="Receita não encontrada")

# Buscar receitas que contenham todos os ingredientes
@router.get("/receitas/all_ingredientes/{ingredientes}", response_model=Page[Receita])
async def busca_por_ingrediente(ingredientes: str):
    receitas = await get_receita_by_ingredientes(Database.get_collection("receitas"), ingredientes.split(",") )
    if receitas:
        return paginate(receitas)
    raise HTTPException(status_code=404, detail="Receita não encontrada")

# Adicionar secao em uma receita (como comentario, avaliacao, dificuldade, etc)
@router.put("/receitas/secao/{receita_id}")
async def adicionar_secao(receita_id: str, secao: Secao):
    receita = await add_secao(Database.get_collection("receitas"), ObjectId(receita_id), secao)
    if receita:
        return {"message": "Seção adicionada", "status_code": status.HTTP_200_OK}
    raise HTTPException(status_code=404, detail="Receita não encontrada")

# Criando a Paginação no retorno da API
add_pagination(router)