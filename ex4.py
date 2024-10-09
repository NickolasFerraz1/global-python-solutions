import json


caminho_arquivo = input("Digite o nome do seu arquivo JSON: ")

with open(f"{caminho_arquivo}.json", 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)


print(dados)
