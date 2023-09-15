#jogo impar par
import random
contador = 0
jogadorvalor = 0
jogadorip = 0
while True:
    print("PAR OU IMPAR")
    jogadorvalor = int(input("digite um valor: "))
    jogadorip = str(input("Qual a aposta? I/P ")).strip().upper() [0]
    pc = random.randint(1,1000)
    print("O computador jogou ", pc)
    soma = jogadorvalor + pc
    if jogadorip == "P":
        if soma %2==0:
            contador += 1
            print("você ganhou!!! você apostou o numero {} e o pc {} = {}".format(jogadorvalor, pc, soma))
        else:
            print("Você perdeuuuuu!!!")
            break
    else:
        if soma %2!=0:
            contador += 1
            print("você ganhou!!! você apostou o numero {} e o pc {} = {}".format(jogadorvalor, pc, soma))
        else:
            print("Você perdeuuuuu!!!")
            break
print("Você venceu {} vezes.".format(contador))