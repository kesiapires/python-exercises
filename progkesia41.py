#Mostrar a categoria dos atletas de natação
from datetime import datetime
ano = int(input("Em que ano você nasceu? "))
anoatual = datetime.now().year
calculo = anoatual - ano
if calculo <= 9 :
    print("Sua categoria é: MIRIM")
elif calculo <= 14 :
    print("Sua categoria é: INFANTIL")
elif calculo <= 19 :
    print("Sua categoria é: JUNIOR")
elif calculo <= 20 :
    print("Sua categoria é: SÊNIOR")
else :
    print("Sua categoria é: MASTER")
