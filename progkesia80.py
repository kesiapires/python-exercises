#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
#já na posição correta de inserção (sem usar o sort()). 
# No final, mostre a lista ordenada na tela.


#tentativa01

#from bisect import bisect
#numlista = []
#for n in range (0, 5):
#    valor = (int(input("Digite um valor: ")))
#    k = numlista.bisect(valor, numlista)
#    numlista.insert(k, valor)
#print(numlista)

lista = []
for n in range(0,5):
    valordig = int(input("Digite um valor: "))
    if n == 0 or valordig > lista[-1]:
        lista.append(valordig)
    else:
        pos = 0
        while pos < len(lista):
            if valordig <= lista[pos]:
                lista.insert(pos, valordig)
                break
            pos+=1
print(f'Os valores digitados em ordem foram: {lista}')

