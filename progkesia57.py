sexo = str(input("Digite seu sexo F/M: ")).strip()
while sexo != "F" and sexo != "M":
    print("digite novamente")
    sexo = str(input("Digite seu sexo F/M: ")).strip()
print("Você é", sexo)