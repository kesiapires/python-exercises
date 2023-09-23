#Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
#o primeiro que indique o número a calcular e outro chamado show, que será um valor 
#lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(numero,show=False):
    '''
--> Calcula o fatorial de um número
:Param numero: o número a ser calculado
:Param show: opcional. Mostra ou não a conta
:Return: o valor do fatorial de um número 'numero' '''

    f = 1
    for c in range(numero,0,-1):
        if show:
            print(c, end='')
            if c > 1:  
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

#main program
print(fatorial(5,show=False))

