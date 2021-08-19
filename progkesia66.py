#crie um programa para ler numeros inteiros, mostra-los e soma-los(desconsiderando o 999)
#999 condição de parada
#USANDO BREAK
s = 0
soma = 0
num = int(input("Digite um valor: "))
while True :
    if num == 999 :
        break
    soma = soma + num
    s += 1
    num = int(input("Digite outro valor: (condição de parada: 999)"))
print("A soma dos {} números inteiros é {}".format(s,soma))



