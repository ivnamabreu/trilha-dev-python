# Funções com parâmetros:
# As funções em Python também podem receber informações externas para trabalhar com diferentes valores. Essas informações são chamadas de parâmetros.
# Os parâmetros permitem deixar a função mais dinâmica, tornando-a mais flexível, reutilizável e poderosa.
# Com parâmetros, a mesma função pode ser usada várias vezes com valores diferentes.
# Ao criar parâmetros:
# Utilize nomes claros
# Evite abreviações desnecessárias
# Pense na reutilização da função

def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("Ana")
saudacao("João")
saudacao("Fernanda")

def apresentar(nome, idade):
    print(f"{nome} tem {idade} anos.")

apresentar("Lucas", 25)
apresentar("Maria", 20)
apresentar("Carlos", 43)