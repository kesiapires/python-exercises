#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

num = (int(input("Digite um valor: ")),int(input("Digite um valor: ")),int(input("Digite um valor: ")),int(input("Digite um valor: "))) 
print(f"Você digitou os numeros: {num}")
print("Os numeros pares digitados foram: ")
for n in num:
    if n %2 == 0 :
        print(n)
print(f"O numero 9 apareceu {num.count(9)} vezes")
if 3 in num :
    print("O numero 3 apareceu pela primeira vez na posição:", num.index(3)+1)
else:
    print("O numero 3 não foi digitado em nenhuma posição")