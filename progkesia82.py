#Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
#respectivamente. Ao final, mostre o conteúdo das três listas geradas.

valores = []
impar = []
par = []
while True:
    num = (int(input("Digite um valor: ")))
    valores.append(num)
    #sem precisar de outro loop
    #if i %2 == 0:
        #par.append(num)
    #if i %2 != 0:
        #impar.append(num)
    simnao = input("Deseja continuar? s/n ")
    if simnao in "Nn":
        break
for i in range(0,len(valores)):
    if i %2 == 0:
        par.append(valores[i])
    if i %2 != 0:
        impar.append(valores[i])
print(f'''Os números da lista são: {valores}
Números pares digitados: {par}
Números impares digitados: {impar}''')
