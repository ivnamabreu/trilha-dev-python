# Módulos:
# São arquivos .py que contêm código Python, como funções, classes e variáveis. 
# Eles são utilizados para organizar melhor o código e separar funcionalidades em diferentes arquivos, *importando um módulo inteiro*.
# A principal ideia dos módulos é dividir o código de maneira lógica.
# Organizar o código em módulos ajuda a:
# facilitar manutenção;
# melhorar leitura;
# reutilizar funções;
# separar responsabilidades;
# tornar o projeto mais organizado.
# Formas de importar:

import conversores #1
from conversores import libras_para_kilogramas #2

print(conversores.kilogramas_para_libras(10))
print(libras_para_kilogramas(100))

#Diferença entre as duas formas:
# 1: útil quando várias funções do módulo serão utilizadas.
# 2: mais prático quando apenas uma função será utilizada.