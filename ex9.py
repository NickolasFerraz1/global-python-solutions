from pymongo import MongoClient
import pytest

# URL de conexão padrão do MongoDB (substitua com a sua URL se estiver usando um MongoDB hospedado)
cliente = MongoClient("mongodb://localhost:27017/")

# Verificar se a conexão foi bem-sucedida

# Acessar um banco de dados (ou criar se não existir)
db = cliente["meu_banco"]

# Acessar (ou criar) uma coleção chamada "alunos"
colecao = db["alunos"]

@pytest.fixture
def setup_database():
    # Limpar a coleção antes de cada teste
    colecao.delete_many({})
    yield
    # Limpar a coleção após cada teste
    colecao.delete_many({})

def delete_aluno(nome):
    try:
        # Deletar o aluno com o nome fornecido
        resultado = colecao.delete_one({"nome": nome})

        # Verificar se o aluno foi deletado e exibir a mensagem apropriada
        if resultado.deleted_count > 0:
            return f"Aluno '{nome}' deletado com sucesso!"
        else:
            return f"Nenhum aluno encontrado com o nome '{nome}'. Verifique o nome e tente novamente."

    except Exception as e:
        print(f"Erro ao conectar ao MongoDB: {e}")

#delete_aluno()

# Teste de Exclusão (Delete)
def test_delete(setup_database):
    doc = {"nome": "Exemplo", "idade": 30}
    colecao.insert_one(doc)
    result = delete_aluno("Exemplo")
    assert result == "Aluno 'Exemplo' deletado com sucesso!"

