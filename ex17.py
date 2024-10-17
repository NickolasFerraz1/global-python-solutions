import pytest
lista = [1, 2, 3, 4, 5, 6]
lista_negativos = [-1, -2, -3, -4, -5, -6]
lista_zero = [0, 0, 0, 0, 0, 0]
lista_um_numero = [10]
lista_vazia = []
def calcular_media(lista):
    if len(lista) == 0:
        return "Lista vazia!"
    else:
            
        a = sum(lista) / len(lista)

        return f"Esta é a média da lista de números: {a}"

#calcular_media(lista_vazia)

def test_calculo_positivos():
    assert calcular_media(lista) == "Esta é a média da lista de números: 3.5"

def test_calculo_negativos():
    assert calcular_media(lista_negativos) == "Esta é a média da lista de números: -3.5"

def test_calculo_zero():
    assert calcular_media(lista_zero) == "Esta é a média da lista de números: 0.0"

def test_calculo_um_numero():
    assert calcular_media(lista_um_numero) == "Esta é a média da lista de números: 10.0"

def test_calculo_lista_vazia():
    assert calcular_media(lista_vazia) == "Lista vazia!"