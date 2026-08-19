# Classes: 
# São estruturas utilizadas para criar novos tipos de objetos dentro do programa. Outras linguagens de programação também utilizam classes como base da programação orientada a objetos.
# Em Python, vários tipos que já utilizamos são classes, como:
# int
# bool
# list
# str
# Criando nossas próprias classes
# O Python permite criar nossas próprias classes e métodos.
# Classes normalmente utilizam:
# Primeira letra maiúscula
# Padrão PascalCase

class Aluno:
     pass

# Criando métodos dentro da classe:
# Métodos são funções definidas dentro da classe.
# Os métodos definem ações e comportamentos dos objetos. Exemplo:
# Aprovar aluno
# Reprovar aluno
# Alterar turma
# Atualizar cadastro

class Aluno:

    def aprovar(self):
        print("Aprovado")

    def reprovar(self):
        print("Reprovado")

# O parâmetro self: 
# Nos métodos, utilizamos o parâmetro self.
# basta entender que ele representa o próprio objeto que está utilizando o método.

# Criando objetos:
# Objetos são criados a partir das classes.
# Esse processo é chamado de instanciação.

aluno_um = Aluno()
aluno_dois = Aluno()

# Utilizando métodos:
# Depois de criar o objeto, podemos executar seus métodos:
# Como métodos são funções, precisamos utilizar parêntese.

aluno_um.aprovar()

# Atributos:
# Além de métodos, objetos também possuem atributos.
# Os atributos representam dados do objeto, por exemplo, como nome, idade etc.

aluno_um.nome = "Maria"
aluno_dois.nome = "José"
aluno_um.idade = 10
aluno_dois.idade = 11
print(aluno_um.nome)
print(aluno_dois.idade)

# Erro:
print(aluno_um.turma) 
# AttributeError: 'Aluno' object has no attribute 'turma'

# Classes ajudam a:
# Organizar o código
# Reutilizar comportamentos
# Modelar dados
# Criar sistemas mais complexos
# Facilitar manutenção
# representar elementos do mundo real, como Usuários, Produtos, Alunos, Contas bancárias, Funcionários e Pedidos.
