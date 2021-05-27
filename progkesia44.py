#calculando o preço do produto e a forma de pagamento
precop = float(input("Qual é o preço do produto? "))
formapag = str(input("""Qual a forma de pagamento? 
1- a vista
2- a vista no cartão
3- 2 vezes no cartão
4- 3 vezes ou mais no cartão
Digite o número desejado: """)).strip().lower()
avista = precop*0.90
avistacartao = precop*0.95
duasxcartao = precop
juros = precop*1.20
if formapag == "1" :
    print("A opção 1 o produto sai a: ",avista)
elif formapag ==  "2" :
    print("A opção 2 o produto sai a: ",avistacartao)
elif formapag == "3" :
    print("A opção 3 o produto sai a: ",duasxcartao)
else :
    print("opção 4 o produto sai a: ",juros)