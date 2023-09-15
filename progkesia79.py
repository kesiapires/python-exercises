#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já exista lá dentro, ele não será adicionado. 
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.


numlista = []
while True:
    numero = (int(input("Digite um valor: ")))
    if numero not in numlista:
        numlista.append(numero)
    simnao = str(input("deseja continuar? s/n"))
    if simnao =="s":
        continue
    else:
        break
numlista.sort()
print(numlista)