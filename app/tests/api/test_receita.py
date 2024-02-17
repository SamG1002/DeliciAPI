from fastapi.testclient import TestClient
from app.models.receita import Receita
from pydantic import ValidationError
from fastapi_pagination import Page
from app.repository.receitas import *
from app.infra.database import Database

# Variaveis de base para testes
receita_id = ""
secao_exemplo = {
    "nome": "string",
    "conteudo": [
        "string"
    ]
}
receita_exemplo =  {
        "nome": "string",
        "secao": [
           secao_exemplo
        ]
    }

# Funcao para validar em laco as receitas paginadas
def validarReceita(response):
    for receita_data in response:
        try:
            Receita(**receita_data)
        except ValidationError as e:
            return False, f"Erro de validação: {e}"
    return True

def test_welcome(client: TestClient) -> None:
    response = client.get("/")
    assert response.status_code == 200

def test_listar_receitas(client: TestClient) -> None:
    response = client.get("/receitas/")
    assert response.status_code == 200
    assert validarReceita(response.json()["items"])

def test_adicionar_receita(client: TestClient):
    global receita_id
    response = client.post("/receitas/", json=receita_exemplo)
    receita_id = response.json()["ObjectId"]
    assert response.status_code == 200
    assert response.json()["message"] == "Receita adicionada com sucesso"

def test_obter_receita(client: TestClient):
    global receita_id
    response = client.get(f"/receitas/{receita_id}")
    assert response.status_code == 200
    assert Receita(**response.json())  
    
def test_atualizar_receita(client: TestClient):
    global receita_id
    response = client.put(f"/receitas/{receita_id}", json=receita_exemplo)
    assert response.status_code == 200
    assert response.json()["message"] == "Receita atualizada com sucesso"

def test_busca_por_ingrediente(client: TestClient):
    ingredientes = "tomate,chocolate,alho"
    response = client.get(f"/receitas/one_ingrediente/{ingredientes}")
    assert response.status_code == 200
    assert validarReceita(response.json()["items"])

def test_busca_todos_ingredientes(client: TestClient):
    # Supondo que você tenha uma string de ingredientes válida
    ingredientes = "leite,chocolate,farinha"
    response = client.get(f"/receitas/all_ingredientes/{ingredientes}")
    assert response.status_code == 200
    assert validarReceita(response.json()["items"])

def test_adicionar_secao(client: TestClient):
    global receita_id
    response = client.put(f"/receitas/secao/{receita_id}", json=secao_exemplo)
    assert response.status_code == 200
    assert response.json()["message"] == "Seção adicionada"

def test_excluir_receita(client: TestClient):
    global receita_id
    response = client.delete(f"/receitas/{receita_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Receita excluida com sucesso"
    