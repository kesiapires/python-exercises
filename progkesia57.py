#Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, 
#mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input("Digite seu sexo F/M: ")).strip() #.lower() [0]
while sexo != "F" and sexo != "M":
#while sexo not in 'MmFf':
    print("digite novamente")
    sexo = str(input("Digite seu sexo F/M: ")).strip() #.lower()
print("Você é", sexo)