import json


alunos = {

    "alunos": [

        {"nome": "Alice", "nota": 9.0},

        {"nome": "Bruno", "nota": 8.5},

        {"nome": "Carla", "nota": 7.8},

        {"nome": "Diego", "nota": 6.9},

        {"nome": "Eva", "nota": 8.2}

    ]

}
with open(f"alunos.json", 'w', encoding='utf-8') as arquivo:
    json.dump(alunos, arquivo, ensure_ascii=False, indent=4)
try:
    caminho_arquivo = input("Digite o nome do seu arquivo JSON: ")

    with open(f"{caminho_arquivo}.json", 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
        print(dados)

except:
    print("Arquivo não encontrado.")
