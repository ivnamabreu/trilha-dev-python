# Métodos de listas:
    # Métodos são funções específicas que utilizamos com determinados tipos de dados - como listas. 
# A sintaxe é diferente das funções tradicionais:
    # usamos a variável + ponto (.) + nome do método
# Principais métodos:
    # append: adiciona um item ao final da lista
    # insert: adiciona um item em uma posição específica (posição, item)
    # remove: adiciona um item em uma posição específica
    # clear: remove todos os elementos da lista
    # pop: remove o último elemento da lista
    # index: retorna o índice da primeira ocorrência de um valor (se o valor não existir, ocorre erro.)
    # count: conta quantas vezes um valor aparece
    # sort: ordena a lista
    # reverse: inverte a ordem da lista 
    # copy: cria uma cópia da lista (alterando a lista original, a cópia não será alterada)
# Verificar valores na lista: in (item in variável)

numeros = [1, 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
numeros.append(1)
numeros.insert(0, 0)
print(numeros)
numeros.remove(1)
print(numeros)
numeros.pop()
print(numeros)
print(numeros.index(3))
print(5 in numeros)
print(numeros.count(7))
numeros.sort()
print(numeros)
numeros.reverse()
print(numeros)
numeros2 = numeros.copy()
print(numeros2)
numeros.clear()
print(numeros)