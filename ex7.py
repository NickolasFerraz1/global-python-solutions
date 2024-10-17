from pymongo import MongoClient
import pytest
from unittest.mock import patch, MagicMock
from pymongo.errors import ConnectionFailure

def conectar_mongodb():
    # URL de conexão padrão do MongoDB (substitua com a sua URL se estiver usando um MongoDB hospedado)
    cliente = MongoClient("mongodb://localhost:27017/")

    # Verificar se a conexão foi bem-sucedida
    try:
        # Listar os bancos de dados disponíveis
        bancos_dados = cliente.list_database_names()
        #print("Conexão bem-sucedida! Bancos de dados disponíveis:")
        return bancos_dados

        
    except Exception as e:
        return f"Erro ao conectar ao MongoDB: {e}"

conectar_mongodb()

@patch('pymongo.MongoClient')
def test_sucesso_conexao(mock_mongo_client):
    # Simulando a lista de bancos de dados com outros bancos adicionais
    mock_mongo_client.return_value.list_database_names.return_value = ['admin', 'local', 'meu_banco']

    # Chama a função que estamos testando
    resultado = conectar_mongodb()

    # Verifica se a lista contém os bancos de dados esperados
    assert 'admin' in resultado
    assert 'local' in resultado
    assert 'meu_banco' in resultado

def test_conectar_mongodb_falha():
    # Simulamos uma falha de conexão
    with patch("pymongo.MongoClient") as mock_mongo_client:
        # Configura o mock para levantar uma exceção de conexão
        mock_client_instance = MagicMock()
        mock_client_instance.list_database_names.side_effect = ConnectionFailure("Falha de conexão")
        mock_mongo_client.return_value = mock_client_instance
        