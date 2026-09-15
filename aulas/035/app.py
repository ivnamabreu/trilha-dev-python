# Os módulos built-in:
# São módulos que já vêm instalados junto com o Python. 
# Isso significa que não precisamos criar esses módulos manualmente nem instalar bibliotecas externas para utilizá-los.
# Esses módulos oferecem funções e classes prontas para diversas tarefas, como:
# geração de números aleatórios;
# manipulação de datas;
# operações matemáticas;
# envio de e-mails;
# conversão de dados;
# geração de senhas;
# entre muitas outras funcionalidades.
# Onde encontrar os módulos do Python?
# https://docs.python.org/3/py-modindex.html

import random

for i in range(3):
    print(random.random())

for i in range(6):
    print(random.randint(10,20))

import random

equipe = [ "Ana", "Fernando", "Felipe", "Tadeu"]
responsavel = random.choice(equipe)
print(responsavel)

#Jogo de Bingo:
import random

bingo = random.sample(range(1,76), 75)
print(bingo)

numeros = list(range(1,76))
sorteados = []
contador = 1
while numeros:
    sorteado = random.choice(numeros)
    sorteados.append(sorteado)
    print(f"{contador} - Número sorteado: {sorteado}")
    numeros.remove(sorteado)
    contador += 1