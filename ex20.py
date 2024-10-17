import pytest
def converter_temperatura(graus, unidade):
    #print("Programa para converter graus Celsius para Fahrenheit ou Kelvin!")
    #graus = float(input("Digite uma temperatura em graus Celsius: "))
    #unidade = input("Digite K caso queira converter para Kelvin, qualquer outro valor para Fahrenheit: ")

    if unidade == "K":
        
        kelvin = graus + 273

        return f"Este é o valor em graus Kelvin: {kelvin}K"
    else:
        
        fahrenheit = (graus * 1.8) + 32

        return f"Este é o valor em graus Fahrenheit: {fahrenheit}°F"

        
#converter_temperatura()

def test_converter_para_kelvin():
    assert converter_temperatura(0, "K") == "Este é o valor em graus Kelvin: 273K"  # 0°C é 273K
    assert converter_temperatura(100, "K") == "Este é o valor em graus Kelvin: 373K"  # 100°C é 373K
    assert converter_temperatura(-273, "K") == "Este é o valor em graus Kelvin: 0K"  # -273°C é 0K

def test_converter_para_fahrenheit():
    assert converter_temperatura(0, "F") == "Este é o valor em graus Fahrenheit: 32.0°F"  # 0°C é 32°F
    assert converter_temperatura(100, "F") == "Este é o valor em graus Fahrenheit: 212.0°F"  # 100°C é 212°F
    assert converter_temperatura(-40, "F") == "Este é o valor em graus Fahrenheit: -40.0°F"  # -40°C é -40°F
