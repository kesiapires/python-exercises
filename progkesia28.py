import random
n = random.randint(1,5)
num = int(input("digite sua guess: "))
if num == n:
    print("você acertou!")
else:   
    print("você errou. O número correto era", n)