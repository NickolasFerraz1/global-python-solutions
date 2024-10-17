import pytest
def verificar_faixa_etaria(idade):

    if idade < 0:
        return "Digite uma idade válida! "
    if idade < 12:
        return "Você é uma criança! "
    elif 12 <= idade <= 17:
        return "Você é um adolescente! "
    elif 18 <= idade <= 64:
        return "Você é um adulto!"
    else:
        return "Você é um idoso!"

#verificar_faixa_etaria()


def test_crianca():
    assert verificar_faixa_etaria(10) == "Você é uma criança! "


def test_adolescente():
    assert verificar_faixa_etaria(13) == "Você é um adolescente! "


def test_adulto():
    assert verificar_faixa_etaria(20) == "Você é um adulto!"


def test_idoso():
    assert verificar_faixa_etaria(80) == "Você é um idoso!"

def test_idade_negativa():
    assert verificar_faixa_etaria(-1) == "Digite uma idade válida! "