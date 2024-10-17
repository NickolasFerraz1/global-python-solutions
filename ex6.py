import pytest
import csv
from unittest.mock import mock_open, patch

def atualizar_csv(indice_pessoa, idade):
    nome_arquivo = 'teste.csv'

    linhas = []
    with open(nome_arquivo, mode='r', encoding='utf-8') as file:
        leitor = csv.reader(file)
        for linha in leitor:
            linhas.append(linha)

    # Ajuste no índice para corresponder ao formato do CSV (ignorando cabeçalhos)
    # Verifica se o índice é válido (não tenta acessar além da lista)
    if 0 <= indice_pessoa < len(linhas):
        linhas[indice_pessoa][1] = idade
    else:
        raise IndexError("Índice fora do alcance")

    # Escreve as linhas atualizadas de volta no arquivo CSV
    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as file:
        escritor = csv.writer(file)
        escritor.writerows(linhas)

    return "Arquivo atualizado com sucesso!"

atualizar_csv(1, "38")
