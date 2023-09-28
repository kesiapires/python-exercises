#Adapte o código do desafio #107, 
#criando uma função adicional chamada moeda() 
#que consiga mostrar os números como um valor monetário formatado.


from exercicio107 import moeda
#main prog
preco = float(input('Digite um preço: '))
print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}')
print(f'Aumentando 10% temos {moeda.moeda(moeda.aumentarPorcent(preco))}')
print(f'Diminuindo 20% temos {moeda.moeda(moeda.diminuirPorcent(preco))}') 

