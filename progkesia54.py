somamaior = 0
somamenor = 0
from datetime import date
data_atual = date.today().year
for i in range (0,7):
    ano = int(input("Em que ano você nasceu? "))
    if data_atual - ano >=18:
        somamaior += 1
    else:
        somamenor += 1
print("{} são maiores de idade e {} são menores de idade".format(somamaior, somamenor))