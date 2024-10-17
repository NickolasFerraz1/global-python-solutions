from pymongo import MongoClient

def delete_aluno():
    # URL de conexão padrão do MongoDB (substitua com a sua URL se estiver usando um MongoDB hospedado)
    cliente = MongoClient("mongodb://localhost:27017/")

    # Verificar se a conexão foi bem-sucedida
    try:
        # Acessar um banco de dados (ou criar se não existir)
        db = cliente["meu_banco"]

        # Acessar (ou criar) uma coleção chamada "alunos"
        colecao = db["alunos"]

        # Solicitar o nome do aluno para deletar
        nome = input("Digite o nome do aluno que deseja deletar: ")

        # Deletar o aluno com o nome fornecido
        resultado = colecao.delete_one({"nome": nome})

        # Verificar se o aluno foi deletado e exibir a mensagem apropriada
        if resultado.deleted_count > 0:
            print(f"Aluno '{nome}' deletado com sucesso!")
        else:
            print(f"Nenhum aluno encontrado com o nome '{nome}'. Verifique o nome e tente novamente.")

    except Exception as e:
        print(f"Erro ao conectar ao MongoDB: {e}")

delete_aluno()