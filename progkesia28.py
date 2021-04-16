import random
n = random.randint(1,5)
num = int(input("digite sua guess de 1 a 5: "))
if num == n:
    print("você acertou!")
else:   
    print("Você errou! O número correto era", n)