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



def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError,TypeError):
            print('\033[4;31m ERRO. Por favor digite um numero inteiro válido!\033[m')
            continue
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError,TypeError):
            print('\033[4;31m ERRO. Por favor digite um numero real válido!\033[m')
            continue
        else:
            return n 


#main prog
ni = leiaInt(f'Digite um número: ')
print(f'Você acabou de digitar o numero inteiro {ni}')
nf = leiaFloat(f'Digite um número: ')
print(f'Você acabou de digitar o numero real {nf}')

