import math
n = int(input("digite um ângulo: "))
s = math.sin(n)
c = math.cos(n)
t = math.tan(n)
print("O ângulo {} tem o seno de {:.2f}, o cosseno de {:.2f} e a tangente {:.2f}".format(n,s,c,t))
