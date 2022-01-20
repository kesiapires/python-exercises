#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados 
#e vai sortear 6 números entre 1 e 60 para cada jogo, 
#cadastrando tudo em uma lista composta.
import random
from time import sleep
print('--'*30)
print(f'M E G A   S E N A')
print('--'*30)
listapalpites = []
palpite = int(input('Quantos palpites você quer? '))
for i in range(0,palpite):
    jogo = []
    for n in range(0,6):
        sorteio = random.randint(1,60)
        jogo.append(sorteio)
    listapalpites.append(jogo)
for n in range(0,palpite):
    sleep(1)
    print(f'O {n+1}º palpite é: {listapalpites[n]}')
