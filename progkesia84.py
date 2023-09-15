# Faça um programa que leia nome e peso de várias pessoas,                                      
# guardando tudo em uma lista. No final, mostre: 

#A) Quantas pessoas foram cadastradas.   
#B) Uma listagem com as pessoas mais pesadas.                                                                                                   
#C) Uma listagem com as pessoas mais leves.


pessoas = []
dado = list()
pleves = ppesadas = 0
while True:
    dado.append(str(input("Digite seu nome: ")))
    dado.append(int(input("Digite seu peso? ")))
    if len(pessoas) == 0:
        pleves = ppesadas = dado[1]
    else:
        if dado[1] > ppesadas:
            ppesadas == dado[1]
        if dado[1] < pleves:
            pleves = dado[1]
    pessoas.append(dado[:])
    dado.clear()
    simnao = str(input("Deseja continuar?")).strip().lower()
    if simnao in "Nn":
        break
print(f'{len(pessoas)} foram cadastradas.')
print(f'{pleves} é a pessoa mais leve da lista.')
print(f'{ppesadas} é a pessoa mais pesada da lista.')


