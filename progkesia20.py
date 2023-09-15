#embaralha o nome de 4 pessoas e faz uma lista com a nova ordem
import random
n1 = input("aluno1: ")
n2 = input("aluno2: ")
n3 = input("aluno3: ")
n4 = input("aluno4: ")
list = [n1,n2,n3,n4]
random.shuffle(list)
print("a ordem de apresentação será: ")
print(list)
