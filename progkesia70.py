#crie um programa que leia o nome e o preço de varios produtos
#O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.
somaprod = 0
prodbarato = 1000000000000000
maior1000 = 0
while True:
    nomeprod = str(input("Digite o nome do produto: ")).strip().lower()
    precoprod = float(input("Didite o valor do produto: "))
    if precoprod > 0 :
        somaprod += precoprod
    if precoprod >= 1000 :
        maior1000 += 1
    if precoprod < prodbarato :
        prodbarato = precoprod
        nomeproduto = nomeprod
    quercontinuar = str(input("Você quer continuar? s/n ")).strip().lower()
    if quercontinuar != "s":
        break
print("""O valor total da compra é: {}
{} produtos custam mais de 1000
O nome do produto mais barato é {} que custa {}""".format(somaprod, maior1000,nomeproduto,prodbarato))


