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

# Função de teste para a função atualizar_csv
def test_atualizar_csv():
    # Simula o conteúdo de um arquivo CSV
    conteudo_csv = "Nome,Idade\nPessoa1,25\nPessoa2,30\nPessoa3,45\n"
    
    # Usa mock_open para simular a leitura e escrita no arquivo
    mock_file = mock_open(read_data=conteudo_csv)
    
    # Patching da função open para usar o mock em vez da real
    with patch("builtins.open", mock_file):
        # Executa a função que atualiza o CSV
        resultado = atualizar_csv(2, "38")  # Atualiza a idade da segunda pessoa

        # Verifica se a função retorna a mensagem correta
        assert resultado == "Arquivo atualizado com sucesso!"
    
