# app/repository/receitas.py
from pymongo.collection import Collection
from app.models.receita import Receita, Secao
from typing import List

def get_receitas(collection: Collection):
    return list(collection.find())

def get_receita_by_id(collection: Collection, receita_id: str):
    return collection.find_one({"_id": receita_id })

def add_receita(collection: Collection, receita: Receita):
    collection.insert_one(receita.dict())

def update_receita(collection: Collection, receita_id: str, receita: Receita):
    collection.update_one({"_id": receita_id}, {"$set": receita.dict()})

def delete_receita(collection: Collection, receita_id: str):
    collection.delete_one({"_id": receita_id})

def get_receita_by_ingrediente(collection: Collection, ingrediente: list):
    filtro = f".*{'|'.join(ingrediente)}.*"
    query = {
                "secao.nome": " Ingredientes",
                "secao.conteudo": {"$regex": filtro, "$options": "i"}
            }
    return list(collection.find(query))

def get_receita_by_ingredientes(collection: Collection, ingredientes: list):
    filtro = "(?=.*" + ")(?=.*".join(ingredientes) + ")"
    query = {
                "secao.nome": " Ingredientes",
                "secao.conteudo": {"$regex": filtro, "$options": "i"}
            }
    return list(collection.find(query))



