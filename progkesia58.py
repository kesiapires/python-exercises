import random
soma = 0
pc = random.randint(1,11)
chute = int(input("digite sua guess de 1 a 10: "))
while chute!= pc : 
    print("Você errou! Tente novamente")
    chute = int(input("digite sua guess de 1 a 10: "))
    soma += 1
print("Você acertou! Foram necessários {} palpites até você acertar.".format(soma))