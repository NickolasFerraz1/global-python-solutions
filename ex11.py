def par_ou_impar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
 
while True:
    try:
        numero = int(input("Digite um número: "))
        break
    except ValueError:
        print("Entrada inválida! Por favor, digite um número inteiro.")
 
resultado = par_ou_impar(numero)
 
if resultado:
    print("O número é par")
else:
    print("O número é ímpar")

par_ou_impar(1)