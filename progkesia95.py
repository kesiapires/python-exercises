#Aprimore o desafio 93 para que ele funcione com vários jogadores, 
#incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

##Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
#O programa vai ler o nome do jogador e quantas partidas ele jogou. 
#Depois vai ler a quantidade de gols feitos em cada partida. 
#No final, tudo isso será guardado em um dicionário, 
#incluindo o total de gols feitos durante o campeonato
jogadores = {}

while True:
    jogador = {}
    jogador['nome'] = str(input("Digite o nome do jogador(a): "))
    partidas = int(input('Quantas partidas '+ jogador['nome']+' jogou? '))
    jogador['partidas'] = []
    jogador['totalgols'] = 0
    for i in range(partidas):
        jogador['partidas'].append(int(input("Quantos gols " + jogador['nome']+ " fez na partida " + str(i+1)+"? ")))
        jogador['totalgols'] += jogador['partidas'][i]
    stop = str(input(' Deseja add um novo jogador? (S/N)')).strip().upper()
    jogadores[jogador['nome']] = jogador
    if stop in 'Nn':
        break
while True:
    nomejogadordetalhe = str(input('Mostrar dados de qual jogador? '))
    jogadordetalhe = jogadores[nomejogadordetalhe]
    for i, v in enumerate(jogador['partidas']):
        print(f'No jogo {(i+1)} fez {v} gols ')
    paracontinua = int(input('Deseja continuar? (999 para parar)'))
    if paracontinua == 999:
        break
    
    