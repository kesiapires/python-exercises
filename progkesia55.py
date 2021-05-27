maior = 0
menor = 50000
for i in range (0, 5):
    peso = float(input("Qual o seu peso? "))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print("O mais pesado pesa {}, e o mais leve pesa {}.".format(maior, menor))
    