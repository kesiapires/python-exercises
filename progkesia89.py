#Crie um programa que leia nome e duas notas de vários alunos 
#e guarde tudo em uma lista composta. 
#No final, mostre um boletim contendo a média de cada um 
#e permita que o usuário possa mostrar as notas de cada aluno individualmente.

diario = []
while True:
    alunos = []
    nome = str(input(f'Digite seu nome: '))
    nota1 = int(input(f'Digite a 1º nota: '))
    nota2 = int(input(f'Digite a 2º nota: '))
    alunos.append(nome)
    alunos.append(nota1)
    alunos.append(nota2)
    diario.append(alunos)
    simnao = str(input(f'Quer continuar digitando? s/n')).lower().strip()
    if simnao in "Nn":
        break
for n in range(0,len(diario)):
    media = (diario[n][1]+diario[n][2])/2
    print('---'*30)
    print(f'{diario[n][0]}')
    print(f'''
    1º nota: {diario[n][1]}
    2º nota: {diario[n][2]}
    Média: {media}''')

