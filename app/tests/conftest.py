import os
from typing import Generator
from fastapi.testclient import TestClient
import pytest
from main import app
from app.routers.receitas import router
from app.infra.database import Database

@pytest.fixture(scope="function")
def client() -> Generator:
    # Abrir Base de Dados
    router.add_event_handler("startup", lambda: Database.connect("localhost:27017", "afrodite"))
    router.add_event_handler("shutdown", Database.disconnect)

    # Definir um TestCLient para definir em todos os testes
    with TestClient(router) as c:
        yield c