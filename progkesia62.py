#melhorearaando o programa 61 perguntando ao usuario  quantos termos mais ele quer visualizar
#só parar quando ele disser que quer ver zero termos 

i = 1
a1 = float(input("Digite o primeiro termo da p.a: "))
r = float(input("Digite a razão da p.a: "))
maistermos = int(input("Você quer ver quantos termos? "))
while maistermos != 0 :
    k = i
    while i <= (k+maistermos-1):
        an=a1+(i-1)*r
        print(an)
        i = i+1
    maistermos = int(input("Você quer ver mais quantos termos? "))
