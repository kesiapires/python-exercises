# Crie um programa que tenha uma tupla única 
#com nomes de produtos e seus respectivos preços, na sequência. 
# No final, mostre uma listagem de preços, 
#organizando os dados em forma tabular.

print("~"*40)
print(f'{"MENÚ":^40}')
print("~"*40)
tabela = ('picole', 1, 'hotdog', 1.5, 'burguer', 4.5, 'coca', 2, 'fries', 2.5, 'pizza', 6, 'juice', 3)
for item in range(0, len(tabela)):
    if item %2 == 0:
       print(f'{tabela[item] :.<25}', end='')
    else:
        print(f'R$:{tabela[item] :>6.2f}')
