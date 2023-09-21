#Faça um programa que tenha uma função chamada área()
#que receba as dimensões de um terreno retangular
#(largura e comprimento) e mostre a área do terreno.

def área(larg,comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m2. ')

    
print('-=-'*20)
print('Controle de terrenos')
print('-=-'*20)
l = float(input("Largura: (m) "))
c = float(input("Comprimento: (m) "))
área(l,c)
