#Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib.request
try:
    webUrl = urllib.request.urlopen('http://pudim.com.br/')
except:
    print('\033[4;31m O site pudim não está acessivel no momento. \033[m')
else:
    print('Consegui acessar o site pudim com sucesso.')