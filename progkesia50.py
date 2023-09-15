#ler 6 numeros inteiros e mostrar apenas os pares
s = 0
for k in range(0,6):
    num = int(input("Digite um número: "))
    if num %2 == 0:
        s += num
print("A soma dos números pares é igual a:",s)