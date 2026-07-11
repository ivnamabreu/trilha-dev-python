# Dicionários
# Os dicionários em Python são estruturas de dados utilizadas para armazenar informações em formato de chave e valor (pares).
# Esse formato facilita a organização, a pesquisa e a manipulação de dados.
# Estrutura do dicionário
# Os dicionários utilizam:
# {} → para delimitar o dicionário
# : → para separar chave e valor
# , → para separar os pares de dados
#Um dicionário pode armazenar diferentes tipos de dados: string, inteiro, boleano, float
# As chaves devem ser únicas
# As chaves de um dicionário não podem se repetir.

aluno = {
    "nome": "Ana",
    "idade": 10,
    "matriculada": True
}
print(aluno["idade"])
aluno["idade"] = 12
print(aluno["idade"])
aluno["turma"] = "A25"
print(aluno["turma"])