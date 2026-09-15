# Módulo pathlib:
# Utilizado para manipular caminhos e arquivos de forma orientada a objetos.
# O pathlib é muito útil para automações, leitura de arquivos, organização de diretórios e processamento de dados.
# Aplicações práticas
# O pathlib pode ser utilizado para:
# Processar planilhas automaticamente
# Ler arquivos CSV
# Organizar diretórios
# Criar automações
# Trabalhar com arquivos de configuração
# Criar scripts utilitários

from pathlib import Path

# A classe Path representa caminhos de arquivos e diretórios.

path1 = Path("aulas/034/ecommerce")
print(path1.exists())

path2 = Path("aulas/036/emails")
print(path2.mkdir())

path3 = Path("aulas/036/emails")
print(path3.rmdir())

# Listando arquivos com glob
# O método .glob() permite localizar arquivos e diretórios utilizando padrões.
# Padrões comuns:
# *	: Todos os arquivos e diretórios
# *.*	: Todos os arquivos
# *.py :	Arquivos Python
# *.csv :	Arquivos CSV
# *.xlsx :	Arquivos Excel

path4 = Path('aulas/034/ecommerce')
for arquivo in path4.glob("*.py"):
    print(arquivo)