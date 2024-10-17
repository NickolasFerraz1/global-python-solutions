import pytest
matriz = [[1,2],
          [4,5]]

def multiplica_matriz(matriz, numero):
    matriz_transf = []
    for i in matriz:
        lista = []
        for num in i:
            num = num * numero
            lista.append(num)
        matriz_transf.append(lista)

    return matriz_transf

# Teste sem usar input
def test_multiplica_matriz_sem_input():
    matriz_esperada = [[2, 4], [8, 10]]
    resultado = multiplica_matriz(matriz, 2)
    assert resultado == matriz_esperada
