#verificando se um numero é ou nao primo
num = int(input("Digite um número: "))
for i in range (1, num):
    if num %num == 1 or num %num == 0:
        print("É um número primo.")
    else:
        print("Não é um número primo")