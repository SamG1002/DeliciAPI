

# :clipboard: Descrição do projeto 
O **DeliciAPI** é uma API em Python utilizando FastAPI, no qual contêm dados de receitas culinárias! 
Tive como objetivo estruturar uma aplicação consistente e eficaz, mesmo que simples.

Utilizei como base de dados o MongoDB utilizando dados do repositório [Afrodite](https://github.com/adrianosferreira/afrodite.json) 

# :rocket: Executar o projeto 

**No terminal, clone o projeto:**
```bash
git clone https://github.com/SamG1002/DeliciAPI.git
```

**Certifique-se de ter o Python (com pip) e MongoDB instalado.**

:warning: [Python](https://www.python.org/downloads/)
:warning: [MongoDB](https://www.mongodb.com/docs/manual/administration/install-community/)

### Configurar ambiente virtual
```bash
python -m venv venv
venv\Scripts\activate
python.exe -m pip install -r requirements.txt
```

## Importar Banco de Dados
```bash
python.exe importa_db.py
```

## Iniciar servidor da API
```bash
uvicorn main:app --reload
```

# :test_tube: Testar o projeto:

### Links e EndPoints
* [Api](http://localhost:8000/)
* [Doc](http://localhost:8000/docs#/)
![image](https://github.com/SamG1002/DeliciAPI/assets/56116583/8eafad80-48a1-4e81-a541-ffd23d151f7a)
  
### Automação dos testes
```bash
pytest
```

# 🧑🏿‍💻 Desenvolvedor

[<img loading="lazy" src="https://github.com/SamG1002/SpotifyML/assets/56116583/cf91dde7-cfad-4acf-9343-a1404eb9148e" width=115><br><sub>Samuel Guerra de Aquino</sub>](https://github.com/SamG1002) 

# Licença 

The [MIT License]() (MIT)

Copyright :copyright: 2024 - DeliciAPI
