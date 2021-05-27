#melhorando o programa 09 da tabuada
#obs ja tinha feito usando "for"
n = int(input("digite um numero: "))

for i in range(0, 10):
    print('{} x {} = {}'.format(n, i, n*i))