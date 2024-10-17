import pytest
def contar_vogais(frase):
    vogais = ["a","A","e","E", "i", "I", "o", "O", "u","U"]
    contador = 0
    if str(frase) == frase:
        for i in frase:
            if i in vogais:
                contador +=1

    else:
        return"Digite uma string válida! " 
    
    return contador

contar_vogais("Teste")

def test_vogais_frase_comum():
    assert contar_vogais("Teste") == 2  # A frase "Teste" tem 2 vogais

def test_vogais_espacos():
    assert contar_vogais("Testando espacos") == 6  # A frase "Testando espacos" tem 5 vogais

def test_vogais_minusculas_maiusculas():
    assert contar_vogais("AEIOUaeiou") == 10  # Todos os caracteres são vogais, total 10

def test_vogais_sem_vogais():
    assert contar_vogais("bcdfg") == 0  # Nenhuma vogal na frase

def test_vogais_frase_vazia():
    assert contar_vogais("") == 0  # String vazia deve retornar 0

def test_vogais_valor_invalido():
    assert contar_vogais(12345) == "Digite uma string válida! "  # Entrada inválida, não é uma string
