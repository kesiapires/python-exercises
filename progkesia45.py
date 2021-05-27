#crie um progama que jogue jokenpô comigo
import random
ppt = str(input("Pedra, papel ou tesoura? ")).lower().strip()
lista = ["pedra", "papel", "tesoura"]
jogo = random.choice(lista)
print("############################################################")
if ppt == "pedra" and jogo == "tesoura" :
    print("você ganhou!! {} vence {}.".format(ppt, jogo))
elif ppt == "tesoura" and jogo == "papel" :
    print("você ganhou!! {} vence {}.".format(ppt, jogo))
elif ppt == "papel" and jogo == "pedra" :
    print("você ganhou!! {} vence {}.".format(ppt, jogo))
elif ppt == jogo :
    print("Empatamos!")
else :
    print("Você perdeu! {} vence {}.".format(jogo, ppt))