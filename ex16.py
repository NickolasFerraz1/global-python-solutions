import pytest
def celsius_para_fahrenheit(graus):
    #print("Programa para converter graus Celsius para Fahrenheit!")
    #graus = float(input("Digite uma temperatura em graus Celsius: "))

    fahrenheit = (graus * 1.8) + 32

    return f"Este é o valor em Fahrenheit: {fahrenheit}°F" 

#celsius_para_fahrenheit()

def test_converter():
    assert celsius_para_fahrenheit(27) == "Este é o valor em Fahrenheit: 80.6°F" 
