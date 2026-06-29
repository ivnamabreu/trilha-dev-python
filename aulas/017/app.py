#Loops aninhados (nested loops)
#Essa estrutura é utilizada quando precisamos repetir uma ação múltiplas vezes dentro de outra repetição.
# Loops aninhados são muito utilizados para comparar dados, como, por exemplo, em valiadações ou processamento de dados.

for x in range(4):
    for y in range(3):
        print(f' ({x}, {y}) ')

for item in ["banana", "maçã", "pera"]:
    for palavra in ["maçã", "uva", "abacaxi"]:
        if item == palavra:
            print(item)
        


#Funcionamento
# O Python executa da seguinte forma:
# 1. Inicia o loop externo;
# 2. Executa completamente o loop interno;
# 3. Incrementa o x;
# 4. Executa novamente o loop interno;
# 5. Repete até finalizar o loop externo.
# Ou seja, o loop interno é executado completamente a cada iteração do loop externo.