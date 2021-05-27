#soma dos numeros impares que sao multiplos de 3 no intervalo de 1 e 500
s = 0
for k in range (1,500):
    if k % 2 != 0 and k %3 == 0:
        s += k
print("A soma dos números ímpares multiplos de 3 é de: ",s)