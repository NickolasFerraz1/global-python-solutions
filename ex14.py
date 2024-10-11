def verificar_nota():
    nota = -1
    while nota < 0 or nota > 100:
        nota = int(input("Digite a sua nota de 0 a 100: "))
        if nota < 0:
            print("Digite uma nota maior que 0")
        
        elif nota > 100:
            print("Digite uma nota menor que 100")

    if nota >= 90:
        print("A")

    elif nota >= 80:
        print("B")
    
    elif nota >= 70:
        print("C")

    elif nota >= 60:
        print("D")
    
    else:
        print("F")
    
verificar_nota()
