# main.py
from fastapi import FastAPI
from app.routers import receitas
from app.infra.database import Database

app = FastAPI(swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})

# Configurar a conexão ao MongoDB ao ciclo de vida da api
app.add_event_handler("startup", lambda: Database.connect("localhost:27017", "afrodite"))
app.add_event_handler("shutdown", Database.disconnect)

# Incluir as rotas de receitas
app.include_router(receitas.router, prefix="/deliciapi", tags=["receitas"])

