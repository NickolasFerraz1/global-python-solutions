from pymongo import MongoClient
import pytest
        
# URL de conexão padrão do MongoDB (substitua com a sua URL se estiver usando um MongoDB hospedado)
cliente = MongoClient("mongodb://localhost:27017/")

# Verificar se a conexão foi bem-sucedida
# Acessar um banco de dados (ou criar se não existir)
db = cliente["meu_banco"]

# Acessar (ou criar) uma coleção chamada "usuarios"
colecao = db["alunos"]


@pytest.fixture
def setup_database():
    # Limpar a coleção antes de cada teste
    colecao.delete_many({})
    yield
    # Limpar a coleção após cada teste
    colecao.delete_many({})


def find_aluno():   
    try:     
        alunos = []
        resultado = colecao.find({"Idade" : {"$gt":30}})
        #print("Todos os alunos com idade maior que 30: ")
        for aluno in resultado:
            alunos.append(aluno)
        return alunos

    except Exception as e:
        print(f"Erro ao conectar ao MongoDB: {e}")

find_aluno()

# Teste de Leitura (Read)
def test_read(setup_database):
    doc = {"nome": "Exemplo", "Idade": 30}
    doc2 = {"nome": "Exemplo2", "Idade": 33}
    doc3 = {"nome": "Exemplo3", "Idade": 29}
    
    # Inserir os documentos na coleção
    colecao.insert_one(doc)
    colecao.insert_one(doc2)
    colecao.insert_one(doc3)
    
    # Chamar a função que estamos testando
    found_docs = find_aluno()
    
    # Verifica se o retorno contém apenas alunos com idade maior que 30
    assert len(found_docs) == 1  # Apenas 1 aluno deve ter idade maior que 30 (doc2)
    
    # Verificação detalhada dos documentos retornados
    for aluno in found_docs:
        assert aluno is not None
        assert aluno["Idade"] > 30
        assert aluno["nome"] == "Exemplo2"