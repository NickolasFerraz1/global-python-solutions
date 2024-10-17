import pytest
def calculadora(num1, num2, operador):

    # print("Escolha uma das operações a seguir: \n")
    # print("1: Soma\n")
    # print("2: Subtração\n")
    # print("3: Divisão\n")
    # print("4: Multiplicação\n")

    while True:

        if operador == 1:
            resultado = num1 + num2
            break
        elif operador == 2:
            resultado = num1 - num2
            break
        elif operador == 3:
            if num2 == 0:
                return "Digite um número válido! "
            else:
                resultado = num1 / num2
                break
        elif operador == 4:
            resultado = num1 * num2
            break
        else:
            return "Digite um número válido! "
    return f"Este é o resultado da sua conta: {resultado}"
#calculadora()

def test_soma_positivos():
    assert calculadora(5, 3, 1) == "Este é o resultado da sua conta: 8"

def test_soma_negativos():
    assert calculadora(-5, -3, 1) == "Este é o resultado da sua conta: -8"

def test_soma_zero():
    assert calculadora(0, 5, 1) == "Este é o resultado da sua conta: 5"


def test_subtracao_positivos():
    assert calculadora(5, 3, 2) == "Este é o resultado da sua conta: 2"

def test_subtracao_negativos():
    assert calculadora(-5, -3, 2) == "Este é o resultado da sua conta: -2"

def test_subtracao_zero():
    assert calculadora(5, 0, 2) == "Este é o resultado da sua conta: 5"


def test_divisao_positivos():
    assert calculadora(6, 3, 3) == "Este é o resultado da sua conta: 2.0"

def test_divisao_negativos():
    assert calculadora(-6, -3, 3) == "Este é o resultado da sua conta: 2.0"

def test_divisao_zero():
    assert calculadora(6, 0, 3) == "Digite um número válido! "  # divisão por zero não permitida


def test_multiplicacao_positivos():
    assert calculadora(5, 3, 4) == "Este é o resultado da sua conta: 15"

def test_multiplicacao_negativos():
    assert calculadora(-5, -3, 4) == "Este é o resultado da sua conta: 15"

def test_multiplicacao_zero():
    assert calculadora(5, 0, 4) == "Este é o resultado da sua conta: 0"
