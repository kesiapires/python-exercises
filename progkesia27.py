nome = str(input("digite seu nome: ")).lower().strip()
cutf = nome.split()[0]
cutl = nome.split()[-1]
print(""" primeiro nome: {}
ultimo nome: {}""".format(cutf,cutl))

# nome = str(input("digite seu nome: ")).lower().strip()
# lista = nome.split()
# cutf = lista[0]
# cutl = lista[-1]
# print(""" primeiro nome: {}
# ultimo nome: {}""".format(cutf,cutl))