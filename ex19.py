import pytest

lista = [1,2,3]
lista_neg = [-3, -2, -1]
lista_zeros = [0, 0]
lista_nula = []
def encontrar_maximo_lista(lista):
    if len(lista) == 0:
        return None
    
    else:
        numero = max(lista)
        return f"Este é o maior número da lista: {numero}"
encontrar_maximo_lista(lista)

def test_maximo_pos():
    assert encontrar_maximo_lista(lista) == "Este é o maior número da lista: 3"

def test_maximo_neg():
    assert encontrar_maximo_lista(lista_neg) == "Este é o maior número da lista: -1"

def test_maximo_zeros():
    assert encontrar_maximo_lista(lista_zeros) == "Este é o maior número da lista: 0"

def test_lista_nula():
    assert encontrar_maximo_lista(lista_nula) == None