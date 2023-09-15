#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
#Guarde esses resultados em um dicionário em Python. 
#No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from random import randint
jogo = {}
for i in range(0,4):
    jogo.append(randint(0,100))
    print(f'Jogador {i+1} tirou {jogo[i]}')
print(jogo)