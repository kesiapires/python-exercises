from exercicio109 import moeda
"""_summary_ Formating function moeda on module moeda
    param1: creating a new parameter reciving a value 'False'
    param2: to shorten the function call

    """
#main prog
preco = float(input('Digite um preço: '))
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}')
print(f'Aumentando 10% temos {moeda.aumentarPorcent(preco, True)}')
print(f'Diminuindo 20% temos {moeda.diminuirPorcent(preco, True)}') 

