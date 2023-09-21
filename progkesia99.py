#Faça um programa que tenha uma função chamada maior(), 
#que receba vários parâmetros com valores inteiros. 
#Seu programa tem que analisar todos os valores e dizer qual deles é o maior.


def maior(*num):
    cont = maior = 0
    print('~~~~>'*10)
    print("\n Analisando os valores passados...")
    for valor in num: 
        print(f'{valor}', end=" ")
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont +=1
    print(f'Foram informados {cont} valores.')
    print(f'O maior valor é {maior}')
    

#main program
maior(1,8,9,5,3,4)
maior(4,9,7,6,2)
maior(6,4)
maior(9)
maior()