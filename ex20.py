def converter_temperatura():
    print("Programa para converter graus Celsius para Fahrenheit ou Kelvin!")
    graus = float(input("Digite uma temperatura em graus Celsius: "))
    unidade = input("Digite K caso queira converter para Kelvin, qualquer outro valor para Fahrenheit: ")

    if unidade == "K":
        
        kelvin = graus + 273

        print(f"Este é o valor em graus Kelvin: {kelvin}K")  

    else:
        
        fahrenheit = (graus * 1.8) + 32

        print(f"Este é o valor em graus Fahrenheit: {fahrenheit}°F")  

        
converter_temperatura()