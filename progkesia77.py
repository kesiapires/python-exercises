 #Exercício Python 077:
 #Crie um programa que tenha uma tupla com várias palavras 
 # (não usar acentos). 
 # Depois disso, você deve mostrar, para cada palavra, 
 # quais são as suas vogais.


print("~"*40)
print(f'{"Palavrinhas" :^30}')
print("~"*40)
palavras = ("porta", "chaveiro", "bicicleta", "casa", "cachorro", "abelha", "amor", "criança", "sapato")
for i in palavras:
    print(f'As vogais da palavra {i} são:')
    for letra in i:
        if letra in 'a':
            print(f'{letra }')
        elif letra in 'e':
            print(f'{letra }')
        elif letra in 'i':
            print(f'{letra }')
        elif letra in 'o':
            print(f'{letra }')
        elif letra in 'u':
            print(f'{letra }')

#resolução do guanabara

#print("~"*40)
#print(f'{"Palavrinhas" :^30}')
#print("~"*40)
#palavras = ("porta", "chaveiro", "bicicleta", "casa", "cachorro", "abelha", "amor", "criança", "sapato")
#for i in palavras:
#    print(f'\nAs vogais da palavra {i} são:', end='')
#    for letra in i:
#        if letra.lower() in 'aeiou':
#           print(letra, end=' ')
