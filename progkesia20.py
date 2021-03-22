import random
n1 = input("digite seu nome: ")
n2 = input("digite seu nome: ")
n3 = input("digite seu nome: ")
n4 = input("digite seu nome: ")
r = random.choices([n1,n2,n3,n4])
print("primeiro lugar {}, segundo lugar {}, terceiro {} e quarto {}".format(r,r,r,r))
