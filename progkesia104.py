#Crie um programa que tenha a função leiaInt(), 
#que vai funcionar de forma semelhante ‘a função input() do Python, 
#só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt(‘Digite um n: ‘)

from colorama import Fore  

def leiaInt(mensagem):
    valorDigitado = input(mensagem)
    while not valorDigitado.isnumeric():
        print(Fore.RED + f' ERRO ')
        print(f'O valor digitado {valorDigitado} não é inteiro. Tente novamente.'+Fore.RESET)
        valorDigitado = input(mensagem)
    return valorDigitado


#main prog
n = leiaInt(f'Digite um número: ')
print(f'Você acabou de digitar o numero {n}')