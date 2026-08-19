# Construtores em classes:
# Permitem definir automaticamente os atributos de um objeto no momento em que ele é criado.
# É um método especial executado automaticamente quando um objeto é criado.
# Em Python, o construtor é definido com: __init__
# Esse método é chamado automaticamente ao iniciar um objeto da classe.

class Aluno:

    def __init__(self, nome, idade, escola = "escola_1"):
        self.nome = nome
        self.idade = idade
        self.escola = escola

# Nesse exemplo:
# __init__ é o construtor;
# nome e idade são parâmetros recebidos;
# self.nome e self.idade criam atributos no objeto.
# Atenção:o self representa o próprio objeto que está sendo criado. E significa:
# criar um atributo chamado nome ou idade, etc no objeto;
# armazenar nele o valor recebido no parâmetro nome/idade/etc.
# Criando objetos com construtor:
# Precisamos informar os valores exigidos pelo construtor:

aluno_um = Aluno("Ana", 14)

# Nesse caso:
# "Ana" será o nome;
# 14 será a idade.
# Se tentarmos criar o objeto sem os parâmetros, o Python gera erro: TypeError

print(aluno_um.nome)
print(aluno_um.idade)
print(aluno_um.escola)
aluno_um.idade = 15
print(aluno_um.nome)
print(aluno_um.idade)
print(aluno_um.escola)

# Mesmo usando construtores, os métodos da classe continuam disponíveis:

class Aluno:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def aprovar(self):
        print("Aprovado")

aluno_um = Aluno("Ana", 14)
aluno_um.aprovar()

# Os construtores ajudam a:
# padronizar objetos;
# evitar repetição;
# garantir atributos obrigatórios;
# organizar melhor o código;
# facilitar manutenção do sistema.