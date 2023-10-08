#Crie um pequeno sistema modularizado que permita cadastrar:
#pessoas pelo nome e idade, em um arquivo de texto simples.
#O sistema só vai ter duas opções:
#cadastrar pessoas, listar todas as pessoas cadastradas e sair do sistema.

from exercicio115.lib.interface import *
from exercicio115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if arquivoExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    criarArquivo(arq)

while True:
    resposta = menu(['ver pessoas cadastradas', 'Cadastrar novas pessoas','Sair do sistema'])
    print(linha())
    if resposta == 1:
        print(f'Opção 1')
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('Opção 2')
    elif resposta == 3:
        print(f'\033[4;36m Saindo do sistema... Até logo!\033[m')
        break
    else:
        print(f'\033[1;31m Erro! Digite uma opção válida.\033[m')
    sleep(2)