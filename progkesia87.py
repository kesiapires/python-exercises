#Aprimore o desafio anterior, mostrando no final:                                                   
# A) A soma de todos os valores pares digitados.                                                              
# B) A soma dos valores da terceira coluna.                                                                                                                
# C) O maior valor da segunda linha.
matriz = [[],[],[]]
somaterceiracoluna = somapares = maiorvalor = 0
for l in range(0,3):
    for c in range(0,3):
        valor = int(input(f'Digite o valor{l,c}: '))
        matriz[l].append(valor)
print(f'{"=-=-" * 30}')
for l in range(0,3):
    somaterceiracoluna += matriz[l][2]
    for c in range(0,3):
        print(f'[{matriz[l][c] :^5}]', end='')
        if matriz[l][c] %2 == 0:
            somapares += matriz[l][c]
        if matriz[1][c]>maiorvalor:
            maiorvalor = matriz[1][c]
    print()

print(f'Soma dos valores pares digitados: {somapares}')
print(f'Soma dos valores da terceira coluna: {somaterceiracoluna}')
print(f'O maior valor da segunda linha é: {maiorvalor}')
print(f'{"=-=-" * 30}')
