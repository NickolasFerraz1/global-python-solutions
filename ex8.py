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

@patch('pymongo.MongoClient')
def test_get_colecao_sucesso(mock_mongo_client):
    # Criar um mock para o cliente do MongoDB
    mock_cliente = MagicMock()

    # Criar um mock para o banco de dados "meu_banco"
    mock_db = MagicMock()

    # Criar um mock para a coleção "alunos"
    mock_colecao = MagicMock()

    # Simular o retorno de find() com alguns documentos de exemplo
    mock_colecao.find.return_value = [
        {'nome': 'João', 'idade': 21},
        {'nome': 'Maria', 'idade': 22}
    ]

    # Configurar o mock do banco de dados para retornar o mock da coleção
    mock_db.__getitem__.return_value = mock_colecao

    # Configurar o cliente mockado para retornar o mock do banco de dados
    mock_cliente.__getitem__.return_value = mock_db

    # Fazer o MongoClient mockado retornar o mock do cliente configurado
    mock_mongo_client.return_value = mock_cliente

    # Chamar a função
    resultado = get_colecao()

    # Verificar se os resultados incluem os alunos esperados
    assert {'nome': 'Marcos', 'idade': 31} in resultado

    # Verificar se o método 'find' foi chamado na coleção "alunos"
    mock_colecao.find.assert_called_once()