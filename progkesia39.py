#informações sobre alistamento militar
#fazer outro desse input lendo a data de nascimento
# idade = int(input("Quantos anos você tem? "))
# if idade == 18 :
#     print("É hora de ir se alistar!")
# elif idade > 18 :
#     maiores = idade - 18
#     print("Já passaram {} anos do tempo de alistamento.".format(maiores))
# elif idade < 18 :
#     menores = 18 - idade
#     print("faltam {} anos para você se alistar".format(menores))

from datetime import datetime
anonascimento = int(input("Em que ano vc was born?"))
anoatual = datetime.now().year
idade = anoatual - anonascimento
if idade == 18 :
     print("É hora de ir se alistar!")
elif idade > 18 :
     maiores = idade - 18
     print("Já passaram {} anos do tempo de alistamento.".format(maiores))
elif idade < 18 :
     menores = 18 - idade
     print("faltam {} anos para você se alistar".format(menores))
