import pytest
def verificar_maior(num1, num2, num3):

    if num1 > num2 and num1 > num3:
        return f"Este é o maior número: {num1}"
    
    elif num2 > num1 and num2 > num3:
        return f"Este é o maior número: {num2}"

    else:
        return f"Este é o maior número: {num3}"



def test_num1_maior():
    assert verificar_maior(3,2,1) == "Este é o maior número: 3"


def test_num2_maior():
    assert verificar_maior(1,3,2) == "Este é o maior número: 3"


def test_num3_maior():
    assert verificar_maior(1,2,3) == "Este é o maior número: 3"

def test_numeros_iguais():
    assert verificar_maior(3, 3, 3) == "Este é o maior número: 3"

def test_num_negativos():
    assert verificar_maior(-1, -5, -3) == "Este é o maior número: -1"
