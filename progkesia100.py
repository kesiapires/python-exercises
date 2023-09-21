#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
#A primeira função vai sortear 5 números e vai colocá-los dentro da lista 
#e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.


from random import randint

def sorteia():
    numeros = []
    for i in range(0,5):
        numeros.append(randint(0,9))
    print(f'Sorteando 5 valores da lista: {numeros}  Pronto!!!')
    return numeros 

def somapar(numeros): 
    pares =0 
    for i in numeros:
        if i %2 == 0:
            pares +=i
    print(f'Somando os valores pares de {numeros} temos: {pares}')

somapar(sorteia())