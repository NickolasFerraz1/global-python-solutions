import pytest
from unittest.mock import mock_open, patch

def ler_csv(caminho):
        
    with open(caminho, "r") as file:
        a = file.read()
        return a

ler_csv("teste.csv")

# Teste da função usando mock
def test_ler_csv():
    # Conteúdo simulado do arquivo CSV
    conteudo_falso = "coluna1,coluna2\nvalor1,valor2"

    # Usando mock para simular a abertura do arquivo
    with patch("builtins.open", mock_open(read_data=conteudo_falso)):
        resultado = ler_csv("teste.csv")
        assert resultado == conteudo_falso