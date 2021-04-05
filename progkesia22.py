nome = input("digite seu nome: ")
#nome = str(input("digite seu nome: ")).strip()
ll = nome.lower()
lu = nome.upper()
#ls = nome.strip()
#ls = len(nome) - nome.count(" ")
lr = nome.replace(" ","")
ls = len(nome.split()[0])
print("""O seu nome em letras minusculas é {}
Letras maiusculas {}
Sem espaços {}
Quantas letras tem o primeiro nome {} letras""".format(ll,lu,lr,ls))