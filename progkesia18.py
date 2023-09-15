''' Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.'''
import math
ang = float(input("digite um angulo: "))
s = math.sin(math.radians(ang))
c = math.cos(math.radians(ang))
t = math.tan(math.radians(ang))
print("O ângulo {} tem o seno de {:.2f}, o cosseno de {:.2f} e a tangente {:.2f}".format(n,s,c,t)

#import math
#n = int(input("digite um valor: "))
#s = math.sin(n)
#c = math.cos(n)
#t = math.tan(n)
#print("O ângulo {} tem o seno de {:.2f}, o cosseno de {:.2f} e a tangente {:.2f}".format(n,s,c,t))
