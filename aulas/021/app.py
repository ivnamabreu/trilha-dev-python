# Tuplas
# Tuplas são estruturas semelhantes às listas, porém são imutáveis, ou seja, não podem ser alteradas após a sua criação.
# Tuplas x Listas:
# A diferença está na sintaxe:
# listas usam colchetes [ ]
# tuplas usam parênteses ( )
# Quando usar tuplas
# Tuplas são úteis quando queremos garantir que os dados não sejam modificados ao longo do programa.
# Métodos disponíveis:
# count
# index
# Por serem imutáveis, métodos como 'append' ou ações de atribuir novos valores a 'índices' estabelecidos na tupla retornam 'erro'.


numeros = (1, 5, 6, 4, 8, 5)
print(numeros.count(5))
print(numeros.count(8))
print(numeros.count(6))
print(numeros.index(1))
print(numeros.index(4))
print(numeros.index(5))
print(numeros[2])
print(numeros[5])
print(numeros[0])