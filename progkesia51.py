#fazer com que o programa leia os 10 primeiros numeros de uma p.a
a1 = float(input("Digite o primeiro termo da p.a: "))
r = float(input("Digite a razão da p.a: "))
print("Esses são os 10 primeros termos da sua p.a: ")
for i in range (0,10) :
    an=a1+(i-1)*r
    print(an)


