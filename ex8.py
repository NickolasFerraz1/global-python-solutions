from pymongo import MongoClient
import pytest
from pymongo.errors import ConnectionFailure
from unittest.mock import patch, MagicMock


# URL de conexão padrão do MongoDB (substitua com a sua URL se estiver usando um MongoDB hospedado)
cliente = MongoClient("mongodb://localhost:27017/")

# Verificar se a conexão foi bem-sucedida

# Acessar um banco de dados (ou criar se não existir)
db = cliente["meu_banco"]

# Acessar (ou criar) uma coleção chamada "alunos"
colecao = db["alunos"]

@pytest.fixture
def setup_database():
    # Limpar a coleção antes de cada teste
    colecao.delete_many({})
    yield
    # Limpar a coleção após cada teste
    colecao.delete_many({})

def get_colecao():
    try:
        # Coletar todos os alunos encontrados
        resultado = colecao.find()
        alunos = [aluno for aluno in resultado]  # Coleta todos os alunos em uma lista
        return alunos

    except Exception as e:
        return f"Erro ao conectar ao MongoDB: {e}"

def test_get_colecao_real():
    try:
        # Executa a função que estamos testando
        alunos = get_colecao()

        # Verifica se a conexão e a consulta ao banco de dados retornam resultados
        assert isinstance(alunos, list), "O retorno deve ser uma lista"
    except ConnectionFailure:
        pytest.fail("Conexão ao MongoDB falhou")