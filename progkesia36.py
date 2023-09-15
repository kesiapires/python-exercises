#aprovando emprestimo bancario para comprar casa
valcasa = float(input("Qual o valor da casa? "))
sal = float(input("Quanto você ganha? "))
tempo = float(input("Em quantos anos você vai pagar? "))
prestacao = valcasa / tempo
minimo = sal *0.30
print("Você vai pagar {:.2f} durante {} anos.".format(prestacao,tempo))
if sal * 0.30 >= prestacao :
    print("Seu empréstimo foi aprovado!")
else :
    print("Infelizmente, seu empréstimo foi negado.")
    print("O mínimo a pagar é ", minimo)