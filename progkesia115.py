#Crie um pequeno sistema modularizado que permita cadastrar:
#pessoas pelo nome e idade, em um arquivo de texto simples.
#O sistema só vai ter duas opções:
#cadastrar pessoas e listar todas as pessoas cadastradas.

from exercicio115.lib.interface import *

while True:
    resposta = menu(['Cadastrar novas pessoas', 'ver pessoas cadastradas'])
    print(linha())