#Adicione o módulo moeda.py criado nos desafios anteriores, 
#uma função chamada resumo(), 
#que mostre na tela algumas informações 
#geradas pelas funções que já temos no módulo criado até aqui.
from exercicio110 import moeda
preco = float(input(f'Digite o preço: R$'))
moeda.resumo(preco,70,20)