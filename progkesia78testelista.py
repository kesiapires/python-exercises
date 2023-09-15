valores = [] #list()
#valores.append(5)
#valores.append(9)
#valores.append(4)
print(valores)
for cont in range(0,5):
    valores.append(int(input("digite um valor: ")))

for c, v in enumerate(valores):
    print(f'na posição {c} encontreio o valor {v}!')
print("cheguei ao final da lista.")