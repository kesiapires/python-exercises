#Crie um programa que declare uma matriz de dimensão 3×3 e 
#preencha com valores lidos pelo teclado. 
#No final, mostre a matriz na tela, com a formatação correta.

matriz = [[],[],[]]
for l in range(0,3):
    for c in range(0,3):
        valor = int(input(f'Digite o valor{l,c}: '))
        matriz[l].append(valor)
print(f'{"=-=-" * 30}')
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c] :^5}]', end='')
    print()
print(f'{"=-=-" * 30}')
