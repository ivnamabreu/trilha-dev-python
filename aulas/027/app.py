# Função return:
# a palavra reservada return devolve resultados para um código executado.
# Sem o return, a função executa o cálculo, mas o resultado não fica disponível para reutilização
# Quando uma função não possui return, o Python devolve automaticamente None.
# Aplicação prática
# Utilize return quando precisar devolver valores
# Prefira funções reutilizáveis
# Evite depender apenas de print()
# Guarde resultados em variáveis quando necessário


def quadrado(numero):
    return numero * numero

print(quadrado(3))

valor = quadrado(3)
print(valor)
