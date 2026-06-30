# Listas:
# Listas são criadas utilizando colchetes [ ]:

nomes = ['Adriana', 'Flávia', 'Jaqueline', 'Maria', 'Ana']
print(nomes)
print(nomes[2])
print(nomes[-1])
print(nomes[3])

# Fatiamento (slicing):
# Regras:
# O início é inclusivo
# O fim é exclusivo
# Se não informar o início, começa do índice 0
# Se não informar o fim, vai até o final
# O slicing não altera a lista original.

print(nomes[:2])
print(nomes[1:4])
print(nomes[2:])

nomes[0] = 'Adriane'
print(nomes)