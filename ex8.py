from pymongo import MongoClient
import pytest
from pymongo.errors import ConnectionFailure
from unittest.mock import patch, MagicMock

def get_colecao():
    # URL de conexão padrão do MongoDB (substitua com a sua URL se estiver usando um MongoDB hospedado)
    cliente = MongoClient("mongodb://localhost:27017/")

    # Verificar se a conexão foi bem-sucedida
    try:
        # Acessar um banco de dados (ou criar se não existir)
        db = cliente["meu_banco"]

        # Acessar (ou criar) uma coleção chamada "alunos"
        colecao = db["alunos"]

        # Coletar todos os alunos encontrados
        resultado = colecao.find()
        alunos = [aluno for aluno in resultado]  # Coleta todos os alunos em uma lista
        return alunos

    except Exception as e:
        return f"Erro ao conectar ao MongoDB: {e}"

get_colecao()

