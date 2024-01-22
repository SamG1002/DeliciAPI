# app/utils/receitas.py
from pymongo.collection import Collection
from app.models.receita import Receita, Secao


def get_receitas(collection: Collection):
    return list(collection.find().limit(10))

def get_receita_by_id(collection: Collection, receita_id: str):
    return collection.find_one({"_id": receita_id })

def add_receita(collection: Collection, receita: Receita):
    collection.insert_one(receita.dict())

def update_receita(collection: Collection, receita_id: str, receita: Receita):
    collection.update_one({"_id": receita_id}, {"$set": receita.dict()})

def delete_receita(collection: Collection, receita_id: str):
    collection.delete_one({"_id": receita_id})
