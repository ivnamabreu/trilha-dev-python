# - Argumentos em funções:
# são os valores enviados para os parâmetros no momento da execução da função.
# Por padrão, os argumentos são posicionais, ou seja, seguem a ordem definida nos parâmetros.
# Também respondem às quantidades de parâmetros definidos na função.
# - Argumentos com palavras-chave (keyword arguments):
# Também podemos informar explicitamente qual valor pertence a cada parâmetro.
# Quando utilizamos palavras-chave, a posição não é mais obrigatória.
# - Esse formato é útil principalmente quando:
# A função possui muitos parâmetros
# Os valores não são tão claros
# Queremos melhorar a legibilidade do código
# - Ao trabalhar com argumentos:
# Utilize palavras-chave em funções complexas
# Prefira legibilidade
# Use nomes claros nos parâmetros
# Evite funções confusas

def apresentar(nome, sobrenome):
    print(nome, sobrenome)

apresentar("Maria", "Abreu")
apresentar("Abreu", "Maria")
# apresentar("Maria") = erro
apresentar(
    nome = "Maria",
    sobrenome = "Abreu"
)
apresentar(
    sobrenome="Abreu",
    nome="Maria"
)

def calcular_custo(
    total_compra,
    valor_entrega,
    desconto
):
    print(f"O valor total da compra foi de {total_compra} reais, com {desconto}% de desconto e {valor_entrega} reais de frete")

calcular_custo(100, 15, 10)
calcular_custo(
    total_compra = 100,
    valor_entrega = 15,
    desconto = 10
)
calcular_custo(100, desconto = 10, valor_entrega = 15)