#Crie um programa onde o usuário possa digitar sete valores numéricos e 
#cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
#No final, mostre os valores pares e ímpares em ordem crescente.

valores = [[], []]
for i in range(0,7):
    num = int(input(f'Digite o {i+1}º valor: '))
    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)
valores[0].sort()
valores[1].sort()
print(f'{"=-" * 30}')
print(f'Todos os valores digitados são: {valores}')
print(f'Valores pares em ordem crescente: {valores[0]}')
print(f'Valores impares em ordem crescente: {valores[1]}')
 