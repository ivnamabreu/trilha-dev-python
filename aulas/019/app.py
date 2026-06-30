# Listas aninhadas (nested lists):
# São estruturas em que cada elemento de uma lista também pode ser outra lista. Esse formato é semelhante ao conceito de matriz
# Esse tipo de estrutura é muito comum quando trabalhamos com dados organizados em tabelas, planilhas ou matrizes.

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz[0])
print(matriz[1][1])
print(matriz[2][2])

matriz[2][2] = 20

for linha in matriz:
    for item in linha:
        print(item)
