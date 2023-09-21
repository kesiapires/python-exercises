#Faça um programa que tenha uma função chamada contador(), 
#que receba três parâmetros: início, fim e passo. 
#Seu programa tem que realizar três contagens através da função criada:  
#a) de 1 até 10, de 1 em 1   
#b) de 10 até 0, de 2 em 2    
#c) uma contagem personalizada
from time import sleep
def contador(inicio, fim, passo):

    print(f'contagem de {inicio} até {fim} de {passo}')
    for i in range(inicio, fim, passo):
        sleep(0.2)
        print(i, end=" ")  
    print('\n')
print(f'{"***"*10}')
contador(1,10,1)
print(f'{"***"*10}')
contador(10,0,-2)
print(f'{"***"*10}')
print(f'Agora é hora de personalizar sua contagem! ')
contador(int(input("Início: ")), int(input("Fim: ")), int(input("Passo: ")))

