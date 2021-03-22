import math

print("Vamos calcular as Raizes da Equacao de 2 grau?? Forma Ax^2 + Bx + C")

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

delta = b*b -4*a*c
x1 = (-b + math.sqrt(delta))/(2*a)
x2 = (-b - math.sqrt(delta))/(2*a)

print ("As raizes sao " + str(x1) + " e " + str(x2))
