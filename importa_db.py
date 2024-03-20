import os
import urllib.request
import json
from pymongo import MongoClient

# url
db = "https://raw.githubusercontent.com/adrianosferreira/afrodite.json/master/afrodite.json"
# Nome do arquivo de backup
name_file = "afrodite.json"

# Diretório do projeto
project_dir = os.path.dirname(os.path.abspath(__file__))
backup_dir = os.path.join(project_dir, "database")

# Se nao existir, cria
if not os.path.exists(backup_dir):
    os.makedirs(backup_dir)

# Baixando arquivo json
urllib.request.urlretrieve(db, os.path.join(backup_dir, name_file))

# Endereco e porta padrao do mongodb
client = MongoClient('localhost', 27017)
db = client['afrodite']
collection = db['receitas']

# Abre o arquivo JSON e insere os documentos na collection
with open(os.path.join(backup_dir, name_file), 'r', encoding='utf-8') as f:
    data = json.load(f)
    # Remover o campo '_id' para gerar um novo
    for document in data:
        if '_id' in document:
            del document['_id']

    print("Importando...")
    # Inserir na collection
    collection.insert_many(data)

print("Importação Concluìda")
client.close()
