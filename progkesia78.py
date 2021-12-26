#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, 
# mostre qual foi o maior e o menor valor digitado 
# e as suas respectivas posições na lista.


numero = []
maior = 0
menor = 80000
for n in range(0,5):
    numero.append(int(input(f'digite um valor: ')))
    #if n == 0:
        #maior = menor = numero[n]
    #else:
        #if numero[n] > maior:
            #maior = numero[n]
        #if numero[n] < menor:
            #menor = numero[n]
    if numero[n] > maior:
        maior = numero[n]
        indmaior = n
    if numero[n] < menor:
        menor = numero[n]
        indmenor = n
print(f'''O maior número da lista é {maior} na posição:{indmaior}
O menor número da lista é {menor} na posição:{indmenor}''')
  

