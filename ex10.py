from pymongo import MongoClient

def find_aluno():
        
    # URL de conexão padrão do MongoDB (substitua com a sua URL se estiver usando um MongoDB hospedado)
    cliente = MongoClient("mongodb://localhost:27017/")

    # Verificar se a conexão foi bem-sucedida
    try:
        # Acessar um banco de dados (ou criar se não existir)
        db = cliente["meu_banco"]

        # Acessar (ou criar) uma coleção chamada "usuarios"
        colecao = db["alunos"]


        
        resultado = colecao.find({"Idade" : {"$gt":30}})
        print("Todos os alunos com idade maior que 30: ")
        for aluno in resultado:
            print(aluno)

    except Exception as e:
        print(f"Erro ao conectar ao MongoDB: {e}")

find_aluno()