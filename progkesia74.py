#gerar 5 numeros aleatorios e guardar numa tupla
#mostrar valor maior e menor
#listar numeros gerados
from random import random
num = (random(), random(), random(), random(), random())
listanum = sorted(num)
print(f"""Numeros gerados:
{num}
O maior foi:
{listanum[-1]}
O menor foi:
{listanum[0]}""")

