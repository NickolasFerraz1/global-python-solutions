import pytest
import json
from unittest.mock import mock_open, patch

# Função que lê um arquivo JSON a partir de um caminho fornecido
def ler_json(caminho_arquivo):
    with open(f"{caminho_arquivo}.json", 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    return dados

# Teste da função usando mock para open
def test_ler_json():
    # Dados JSON simulados
    dados_falsos = {"nome": "Teste", "idade": 30}

    # Usando mock para simular a leitura do arquivo
    with patch("builtins.open", mock_open(read_data=json.dumps(dados_falsos))):
        resultado = ler_json("arquivo_teste")
        assert resultado == dados_falsos
