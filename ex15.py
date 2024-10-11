def calculadora():
    num1 = int(input("Digite o primeiro número que deseja realizar um cálculo: "))

    num2 = int(input("Digite o segundo número que deseja realizar um cálculo: "))
    
    print("Escolha uma das operações a seguir: \n")
    print("1: Soma\n")
    print("2: Subtração\n")
    print("3: Divisão\n")
    print("4: Multiplicação\n")

    while True:
        operador = int(input("Digite qual operação deseja realizar: "))

        if operador == 1:
            resultado = num1 + num2
            break
        elif operador == 2:
            resultado = num1 - num2
            break
        elif operador == 3:
            resultado = num1 / num2
            break
        elif operador == 4:
            resultado = num1 * num2
            break
        else:
            print("Digite um número válido! ")
    print(f"Este é o resultado da sua conta: {resultado}")
calculadora()