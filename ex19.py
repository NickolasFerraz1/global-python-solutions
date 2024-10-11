lista = [1,2,3]
def encontrar_maximo_lista(lista):
    if len(lista) == 0:
        print(None)
    
    else:
        numero = max(lista)
        print(f"Este é o maior número da lista: {numero}")

encontrar_maximo_lista(lista)