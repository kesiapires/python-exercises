#Faça um mini-sistema que utilize o Interactive Help do Python. 
#O usuário vai digitar o comando e o manual vai aparecer. 
#Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. 
#Importante: use cores.
c = ('\033[0;30;40m', #branco
     '\033[0;30;41m', #vermelho 
     '\033[0;30;42m', #verde
     '\033[0;30;43m', #amarelo
     '\033[0;30;44m', #azul
     '\033[0;30;45m', #roxo
     '\033[m', #sem cores
     '\033[0;30;47m', #cinza
)
def ajuda(command):
    titulo(f'Acessando o manual do comando \{command}\'', 4)
    print(c[7], end='')
    help(command)
    print(c[6], end='')


def titulo(msg, cor=0):
    tam = len(msg) + 6 
    print(c[cor], end='')
    print('-'* tam)
    print(f'   {msg}')
    print('-'* tam)
    print(c[6], end='')

#main prog
while True:
    titulo('Sistema de ajuda PyHelp', 2)
    comando = str(input(f'Função ou biblioteca: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até logo!',1)