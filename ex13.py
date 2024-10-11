def verificar_faixa_etaria():
    idade = -1
    while idade < 0:
        idade = int(input("Digite sua idade: "))
        if idade < 0:
            print("Digite uma idade válida! ")
    if idade < 12:
        print("Você é uma criança! ")
    elif 12 <= idade <= 17:
        print("Você é um adolescente! ")
    elif 18 <= idade <= 64:
        print("Você é um adulto!")
    else:
        print("Você é um idoso!")

verificar_faixa_etaria()