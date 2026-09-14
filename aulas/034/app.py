# Pacotes: 
# São uma forma de organizar o código Python em diretórios. Eles funcionam como “pastas especiais” que agrupam módulos relacionados. 
# A ideia dos pacotes é facilitar a organização de projetos maiores, separando funcionalidades em diferentes partes do sistema.
# Por que usar pacotes?
# Pacotes ajudam a:
# oganizar projetos maiores;
# separar funcionalidades;
# facilitar manutenção;
# melhorar reutilização do código;
# tornar a navegação do projeto mais simples.
# Além disso, frameworks e bibliotecas Python utilizam bastante essa estrutura.

from ecommerce.entrega import calculadora_entrega #1 
from ecommerce import entrega #2 

calculadora_entrega()
entrega.calculadora_entrega()