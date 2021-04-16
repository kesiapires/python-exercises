#verificando se da pra formar um triangulo com o valor dos vertices
r0 = float(input("digite um valor: "))
r1 = float(input("digite um valor: "))
r2 = float(input("digite um valor: "))
if r0 > r1 + r2 and r1 > r2 + r0 and r2 > r1 + r0:
    print("Não foi possível formar um triângulo com esses valores.")
#elif r0 < r1 + r2 and r1 < r2 + r0 and r2 < r1 + r0:
else:
    print("Você conseguiu formar um triângulo!")
#if r0>(r1+r2):
    #print("não é possivel formar um triangulo")
#elif r1>(r0+r2):
    #print("não é possivel formar um triangulo")
#elif r2>(r1+r0):
    #print("não é possivel formar um triangulo")

#if r0<(r1+r2):
    #print("é possivel formar um triangulo")
#elif r1<(r0+r2):
    #print("é possivel formar um triangulo")
#elif r2<(r1+r0):
    #print("é possivel formar um triangulo")
