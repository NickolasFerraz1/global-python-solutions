import csv


nome_arquivo = 'teste.csv'


linhas = []
with open(nome_arquivo, mode='r', encoding='utf-8') as file:
    leitor = csv.reader(file)
    for linha in leitor:
        linhas.append(linha)

pessoa = int(input("Digite o número da pessoa que deseja alterar a idade (A partir de 1): "))
linhas[pessoa][1] = input("Digite a Idade que deseja alterar: ")  


with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as file:
    escritor = csv.writer(file)
    escritor.writerows(linhas)

print("Arquivo atualizado com sucesso!")
