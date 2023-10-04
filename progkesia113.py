#Reescreva a função leiaInt() que fizemos no desafio 104, 
#incluindo agora a possibilidade da digitação de um número de tipo inválido. 
#Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

#from colorama import Fore  

# def leiaInt(mensagem):
#     valorDigitado = input(mensagem)
#     while not valorDigitado.isnumeric():
#         print(Fore.RED + f' ERRO ')
#         print(f'O valor digitado {valorDigitado} não é inteiro. Tente novamente.'+Fore.RESET)
#         valorDigitado = input(mensagem)
#     return valorDigitado

from exercicio113.intAndFloat import leiaInt, leiaFloat

#main prog
ni = leiaInt(f'Digite um número: ')
print(f'Você acabou de digitar o numero inteiro {ni}')
nf = leiaFloat(f'Digite um número: ')
print(f'Você acabou de digitar o numero real {nf}')

