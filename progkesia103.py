#Faça um programa que tenha uma função chamada ficha(), 
#que receba dois parâmetros opcionais: o nome de um jogador e 
#quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, 
#mesmo que algum dado não tenha sido informado corretamente.

def ficha(jog='desconhecido', gols=0):
    print(f'O jogador {jog} fez {gols} gols no campeonato.')

nome = str(input(f'Nome do jogador: '))
g = input(f'Número de gols: ')
if g.isnumeric():
    g = int(g)
else:
    g = 0
if nome.strip() == '':
    ficha(gols=g)
else:
    ficha(nome, g)


