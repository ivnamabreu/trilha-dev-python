# Herança:
# É um mecanismo da programação orientada a objetos que permite que uma classe herde atributos e métodos de outra classe. 
# Isso evita repetição de código e facilita a reutilização de comportamentos comuns entre diferentes classes.
# A ideia é evitar redundância no código, ou utilizar o princípio DRY: Don't Repeat Yourself
# Para resolver a repetição, cria-se uma classe mais genérica, da qual outras classes podem herdar seu comportamento: 

class Animal:

    def passear(self):
        print("Passear")

class Cachorro(Animal):
    pass

class Gato(Animal):
    pass

# A sintaxe da herança funciona colocando a classe pai entre parênteses.
# Como as classes ficaram vazias, foi utilizado o pass, que funciona como um placeholder e indica ao Python que aquela classe existe, mesmo sem implementação no momento.
# Mesmo sem definir o método passear dentro de Cachorro, o objeto consegue utilizá-lo porque herdou da classe Animal:

caramelo_um = Cachorro()
caramelo_um.passear()

# Além dos métodos herdados, cada classe filha também pode ter métodos próprios:

class Cachorro(Animal):

    def latir(self):
        print("Au au")

caramelo_um = Cachorro()

caramelo_um.passear()
caramelo_um.latir()

# A herança ajuda a:
# evitar repetição de código
# reutilizar comportamentos
# facilitar manutenção
# organizar melhor o sistema
# criar estruturas mais reutilizáveis