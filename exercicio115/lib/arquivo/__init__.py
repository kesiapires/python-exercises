from exercicio115.lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('\033[4;31m Houve um ERRO na criação do arquivo. \033[m')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(f'Não foi possível ler o arquivo {nome}')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        print(a.readlines())