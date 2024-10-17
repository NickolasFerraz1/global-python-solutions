import pytest

def par_ou_impar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

# Esta função é para interagir com o usuário
def solicita_numero():
    while True:
        try:
            numero = int(input("Digite um número: "))
            return numero
        except ValueError:
            print("Entrada inválida! Por favor, digite um número inteiro.")

if __name__ == "__main__":
    numero = solicita_numero()
    resultado = par_ou_impar(numero)

    if resultado:
        print("O número é par")
    else:
        print("O número é ímpar")

def test_par_ou_impar_par():
    assert par_ou_impar(2) == True  # Testa se 2 é par

def test_par_ou_impar_impar():
    assert par_ou_impar(3) == False  # Testa se 3 é ímpar

def test_par_ou_impar_zero():
    assert par_ou_impar(0) == True  # Testa se 0 é considerado par