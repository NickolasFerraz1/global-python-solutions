import pytest
matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]
def matriz(matriz):
    return matriz

matriz(matriz)

def test_matriz():
    matriz_esperada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    resultado = matriz(matriz_esperada)
    assert resultado == matriz_esperada

def test_matriz_vazia():
    assert matriz([]) == []

def test_matriz_unitaria():
    assert matriz([[1]]) == [[1]]
