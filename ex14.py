import pytest
def verificar_nota(nota):
    if nota < 0:
        return "Digite uma nota maior que 0"
    
    elif nota > 100:
        return "Digite uma nota menor que 100"

    if nota >= 90:
        return "A"

    elif nota >= 80:
        return "B"
    
    elif nota >= 70:
        return "C"

    elif nota >= 60:
        return "D"
    
    else:
        return "F"
    
#verificar_nota()

def test_a():
    assert verificar_nota(90) == "A"


def test_b():
    assert verificar_nota(80) == "B"


def test_c():
    assert verificar_nota(70) == "C"


def test_d():
    assert verificar_nota(60) == "D"


def test_f():
    assert verificar_nota(50) == "F"

def test_maior_100():
    assert verificar_nota(101) ==  "Digite uma nota menor que 100"

def test_menor_0():
    assert verificar_nota(-1) == "Digite uma nota maior que 0"