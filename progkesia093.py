##Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
#O programa vai ler o nome do jogador e quantas partidas ele jogou. 
#Depois vai ler a quantidade de gols feitos em cada partida. 
#No final, tudo isso será guardado em um dicionário, 
#incluindo o total de gols feitos durante o campeonato

jogador = {}
jogador['nome'] = str(input("Digite o nome do jogador(a): "))
partidas = int(input('Quantas partidas '+ jogador['nome']+' jogou? '))
jogador['partidas'] = []
jogador['totalgols'] = 0
for i in range(partidas):
    jogador['partidas'].append(int(input("Quantos gols " + jogador['nome']+ " fez na partida " + str(i+1)+"? ")))
    jogador['totalgols'] += jogador['partidas'][i]
for k,v in jogador.items():
    print(f'{k} = {v}')