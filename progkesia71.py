#banco
#dar cedulas 50 20 10 1
contvalorsacado = 0
cedulas = [50,20,10,1]
notas = [0,0,0,0]

while True:
    print('*' *30)
    print("BANCO KESIA")#{:^20}
    print("***************************************")
    valorsacado = int(input("Que valor você quer sacar? R$"))
    total = valorsacado 
    index = 0
    for i in cedulas:
        if total >= i:
            notas[index] = total // i 
            total = total % i   
        index += 1
    print("""Aqui estão suas notas: 
    {} notas de 50 reais
    {} notas de 20 reais
    {} notas de 10 reais
    {} notas de 1 real""".format(notas[0], notas[1], notas[2], notas[3]))
    desejacont = str(input("Deseja continuar a operação? s/n")).strip().lower()
    if desejacont != "s":
        break 



   