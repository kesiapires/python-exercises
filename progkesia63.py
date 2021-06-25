#mostrar a sequencia de fibonacci
s = 2
num = int(input("Digite um número para ver a sequência de fibonacci: "))
f1 = 0
f2 = 1
print("O {} termo de Fibonacci é: {} ".format(num, f1))
print("O {} termo de Fibonacci é: {} ".format(num, f2))
while s < num:
    soma = f1 + f2 
    f1 = f2
    f2 = soma
    print("O {} termo de Fibonacci é: {} ".format(num, soma))
    s += 1

