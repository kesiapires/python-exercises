#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
#Seu aplicativo deverá analisar se a expressão está com os parênteses abertos e fechados na ordem correta.


parenteses = []
expressao = str(input("Digite uma expressão: "))
for i in expressao:
    if i == "(":
        parenteses.append(i)
    if i == ")":
        if len(parenteses) == 0:
            print("Expressão incorreta")
            break
        else:
            parenteses.pop()
if len(parenteses) == 0:
    print(f'Expressão correta!')
else:
    print(f'Expressão incorreta.')



