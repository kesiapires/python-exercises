#criar um programa q leia a idade e o sexo de varias pessoas
#A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.
contmulhermenos20 = 0
conthomem = 0
contmaiorde18 = 0
#sexo = " "
while True:
    print("CADASTRE UMA PESSOA")
    #while sexo not in "mf":
    sexo = str(input("Digite seu sexo: f/m ")).strip().lower()
    idade = int(input("Digite sua idade: "))
    if sexo == "m":
        conthomem += 1 
    if idade >= 18:
        contmaiorde18 += 1
    if sexo == "f" and idade < 20:
        contmulhermenos20 += 1
    quercontinuar = str(input("Quer continuar? "))
    if quercontinuar == "n":
        break 
print("{} homens foram cadastrados.".format(conthomem))
print("{} pessoas tem mais de 18".format(contmaiorde18))
print("{} mulheres tem menos de 20".format(contmulhermenos20))