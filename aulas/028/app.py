# Tratando erros em Python
# Durante a execução de um programa, erros podem acontecer. Alguns desses erros são previsíveis e podem ser tratados para evitar que o programa pare de funcionar.
# Para isso, o Python oferece a estrutura try e except.
# Erros comuns: ValueError e ZeroDivisionError

# Estrutura do try e except: 
#try:
    # código que pode gerar erro

# except TipoDoErro:
    # tratamento do erro

# except TipoDoErro:
    # tratamento do erro

# *Indentação é obrigatória

# Por que tratar erros?
# O tratamento de erros permite:
# Evitar que o programa pare inesperadamente
# Melhorar a experiência do usuário
# Criar sistemas mais estáveis
# Exibir mensagens mais amigáveis
# Exemplos comuns no dia a dia
# Tratamento de erros é muito usado em:
# Login de usuários
# Cadastro de contas
# Validação de e-mails
# Formulários
# Sistemas bancários
# APIs
# Aplicação prática
# Ao tratar erros:
# Leia sempre a mensagem do erro
# Trate apenas erros previsíveis
# Mostre mensagens claras para o usuário
# Evite deixar o programa encerrar inesperadamente

idade = int(input("Idade: "))
print(idade)

try:
    idade = int(input("Idade: "))
    print(idade)

except ValueError:
    print("Idade inválida")

try:
    idade = int(input("Idade: "))

    salario = 10000

    print(salario / idade)

except ValueError:
    print("Idade inválida")

except ZeroDivisionError:
    print("A idade não pode ser zero")