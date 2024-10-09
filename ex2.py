numero = int(input("Digite um número de 1 a 10: "))
matriz = [[1,2],
          [4,5]]

matriz_transf = []
for i in matriz:
    lista = []
    for num in i:
        num = num*numero
        lista.append(num)
    matriz_transf.append(lista)

print(matriz_transf)
