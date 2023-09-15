#TABUADA
i = 0
contador = 0
while True:
    numero = int(input("Quer ver a tabuada de qual valor? "))
    if numero < 0 :
        break
    for i in range (0,11):
        result = i * numero
        print("""{} x {} = {} """.format(i,numero,result))