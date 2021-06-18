#Desenvolva um programa que leia o nome,
#idade e sexo de 4 pessoas. No final do programa, 
# mostre: a média de idade do grupo, qual é o nome 
# do homem mais velho e quantas mulheres têm menos de 20 anos.
ageman = 0
medage = 0
woman = 0
nnome = 0
for i in range(1,5):
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))
    medage += idade
    sexo = str(input("Digite seu sexo (m/f): ")).lower()
    if sexo == "m" or sexo == "masculino":
         if idade > ageman:
            ageman = idade
            nnome = nome
    if sexo == "feminino" or sexo == "f":
            if idade <= 20:
                woman += 1
print("""A média da idade do grupo é {}
O nome do homem mais velho é {}
{} mulheres tem menos de 20 anos.
""".format(medage/4,nnome,woman))