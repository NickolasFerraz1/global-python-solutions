def contar_vogais(frase):
    vogais = ["a","A","e","E", "i", "I", "o", "O", "u","U"]
    contador = 0
    if str(frase) == frase:
        for i in frase:
            if i in vogais:
                contador +=1

    else:
        print("Digite uma string válida! ")
        return 
    
    print(f"Esta é a quantidade de vogais presentes na string: {contador}")

contar_vogais("Teste")