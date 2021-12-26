#Crie um programa que vai ler vários números e colocar em uma lista.                  
#Depois disso, mostre:                
#A) Quantos números foram digitados.                                               
#B) A lista de valores, ordenada de forma decrescente. 
#C) Se o valor 5 foi digitado e está ou não na lista.

listanum = []
while True:
    listanum.append(int(input("Digite um valor: ")))
    simnao = str(input("Deseja continuar? s/n "))
    if simnao in "Nn":
        break
listanum.sort(reverse=True)
print(f'''Quantidade de números digitados: {len(listanum)}
Os valores em ordem decrescente são: {listanum}''') 
if 5 in listanum:
    print(f'o número 5 foi encontrado na lista')
else:
    print(f'o número 5 não foi encontrado na lista')