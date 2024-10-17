import pytest
import json
from unittest.mock import mock_open, patch

alunos = {
    "alunos": [
        {"nome": "Alice", "nota": 9.0},
        {"nome": "Bruno", "nota": 8.5},
        {"nome": "Carla", "nota": 7.8},
        {"nome": "Diego", "nota": 6.9},
        {"nome": "Eva", "nota": 8.2}
    ]
}

def escrever_json(caminho):
    """Escreve os dados de alunos em um arquivo JSON."""
    with open(caminho, 'w', encoding='utf-8') as arquivo:
        json.dump(alunos, arquivo, ensure_ascii=False, indent=4)

def ler_json(caminho_arquivo):
    """Lê um arquivo JSON e retorna o conteúdo."""
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            return dados
    except FileNotFoundError:
        return "Arquivo não encontrado."

# Teste da função escrever_json
def test_escrever_json():
    # Simular o comportamento da função open
    with patch("builtins.open", mock_open()) as mocked_file:
        escrever_json("alunos.json")

        # Captura todas as chamadas para 'write'
        handle = mocked_file()

        # Concatenar todas as chamadas de write
        escrita_final = "".join(call.args[0] for call in handle.write.call_args_list)

        # Verificar se o conteúdo escrito é o esperado
        esperado = json.dumps(alunos, ensure_ascii=False, indent=4)
        assert escrita_final == esperado


# Testando a função ler_json
def test_ler_json():
    # Simular os dados lidos de um arquivo JSON
    dados_falsos = json.dumps(alunos)
    
    with patch("builtins.open", mock_open(read_data=dados_falsos)) as mocked_file:
        resultado = ler_json("alunos.json")

        # Verifica se a função open foi chamada corretamente
        mocked_file.assert_called_once_with("alunos.json", 'r', encoding='utf-8')

        # Verifica se o conteúdo lido está correto
        assert resultado == alunos

# Testando a função ler_json para um arquivo inexistente
def test_ler_json_arquivo_nao_encontrado():
    with patch("builtins.open", side_effect=FileNotFoundError):
        resultado = ler_json("arquivo_inexistente.json")

        # Verifica se a função retorna a mensagem correta quando o arquivo não é encontrado
        assert resultado == "Arquivo não encontrado."
