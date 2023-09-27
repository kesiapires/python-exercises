#Crie um módulo chamado moeda.py que tenha as funções incorporadas
# aumentar(), diminuir(), dobro() e metade(). 
#Faça também um programa que importe esse módulo e use algumas dessas funções.

from exercicio107 import moeda
#main prog
preco = float(input('Digite um preço: '))
print(f'A metade de {preco} é {moeda.metade(preco)}')
print(f'O dobro de {preco} é {moeda.dobro(preco)}')
print(f'Aumentando 10% temos {moeda.aumentarPorcent(preco)}')
print(f'Diminuindo 20% temos {moeda.diminuirPorcent(preco)}') 

