from pymongo import MongoClient

# URL de conexão padrão do MongoDB (substitua com a sua URL se estiver usando um MongoDB hospedado)
cliente = MongoClient("mongodb://localhost:27017/")

# Verificar se a conexão foi bem-sucedida
try:
    # Listar os bancos de dados disponíveis
    bancos_dados = cliente.list_database_names()
    print("Conexão bem-sucedida! Bancos de dados disponíveis:")
    print(bancos_dados)

    
except Exception as e:
    print(f"Erro ao conectar ao MongoDB: {e}")
