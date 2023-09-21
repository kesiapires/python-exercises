#Crie um programa que leia nome, sexo e idade de várias pessoas, 
#guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
#No final, mostre: 
#A) Quantas pessoas foram cadastradas 
#B) A média de idade 
#C) Uma lista com as mulheres 
#D) Uma lista de pessoas com idade acima da média
cadastro = []
idade = 0
mulheres = []
while True:
    pessoa = {}
    pessoa['nome'] = str(input('Digite seu nome: '))
    pessoa['idade'] = int(input('Digite sua idade: '))
    pessoa['sexo'] = str(input('sexo: (F/M) ')).strip().upper()
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
    cadastro.append(pessoa)
    idade +=pessoa['idade']
    simounao = str(input('Deseja cadastrar mais alguém? (S/N) '))
    if simounao in 'Nn':
        break
print(f'Foram cadastradas {len(cadastro)} pessoas')
print('A média da idade das pessoas cadastradas é de: '+ str(idade/len(cadastro)))
print(f'As mulheres cadastradas são: {mulheres}')  
print(f'As pessoas com a idade acima da média são: {idade}')
print(cadastro)
