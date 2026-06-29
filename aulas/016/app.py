# For:
# Utilizado para percorrer elementos de uma sequência. 
# Pode ser entendido como: “para cada item” dentro de uma coleção.

# Diferença em relação ao while
# O while depende de uma condição
# O for percorre uma sequência com fim definido

# Resumo
# for percorre elementos de uma sequência
# A variável de loop (ex: item) representa cada elemento
# in indica a coleção a ser percorrida
# A coleção pode ser:
# string
for item in "Python":
    print(item)

# lista
for item in ["banana", "maçã", "abacate"]:
    print(item)

for item in [1, 5, 9]:
    print(item)

# range (série, sequência, intervalo): pode-se definir um número/tamanho, início e fim, ou ainda um step (passo/forma de contagem)
# o primeiro entra, o último não entra.
for item in range(10):
    print(item)

for item in range(1, 11):
    print(item)

for item in range(1, 11, 2):
    print(item)

# break: interrompe o loop
# continue: pula a itereção (cria uma exceção)

for numero in range(1,10):
    if numero == 3:
        break
    print (numero)
print('fim')

for numero in range(1,10):
    if numero == 3:
        continue
    print (numero)
print('fim')