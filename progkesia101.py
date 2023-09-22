#Crie um programa que tenha uma função chamada voto() 
#que vai receber como parâmetro o ano de nascimento de uma pessoa, 
#retornando um valor literal indicando se uma pessoa tem voto NEGADO, 
#OPCIONAL e OBRIGATÓRIO nas eleições.

#frist try
# def voto(nascimento):
#     import datetime
#     anoNascimento = int(input(f'Digite sua data de nascimento:    (Só números, DDMMAAAA)'))
#     dataAtual = datetime.date.today()
#     calculoIdade = dataAtual - anoNascimento
#     if calculoIdade < 16:
#         print(f'Voto NEGADO. Você ainda não pode votar, pois só tens {calculoIdade} anos.')
#     if calculoIdade >= 16 < 18:
#         print(f'Voto OPCIONAL.')
#     if calculoIdade >=18: 
#         print(f'Voto Obrigatório')    
#     return(calculoIdade)



#second try
# def voto():
#     import datetime
#     dataAtual = datetime.date.today()
#     global calculoIdade
#     calculoIdade = dataAtual - anoNascimento   
#     return(calculoIdade)

# anoNascimento = int(input(f'Digite sua data de nascimento:    (Só números, DDMMAAAA)'))
# if calculoIdade < 16:
#     print(f'Voto NEGADO.')
# if calculoIdade >= 16 < 18:
#     print(f'Voto OPCIONAL.')
# if calculoIdade >=18: 
#     print(f'Voto OBRIGARTÓRIO.')



#third try
import datetime
def voto(anoNascimento):
    dataAtual = datetime.date.today().year
    calculoIdade = dataAtual - anoNascimento   
    if calculoIdade < 16:
        return 'NEGADO'
    if calculoIdade in range(16,18):
        return 'OPCIONAL'
    if calculoIdade >=18: 
        return 'OBRIGATÓRIO'

print(f'Voto', voto(int(input(f'Digite seu ano de nascimento:    (Só números, AAAA)'))))
