num1 = int(input("Digite um valor: "))
num2 = int(input("Digite um valor: "))
print
menu = int(input("""Menu:
1 somar
2 multiplicar
3 maior
4 trocar numeros
5 sair do programa """))
while menu != 5 :
    if menu == 1:
        soma = num1 + num2
        print("++++++++++++++++++++++++++")
        print(soma)
        print("++++++++++++++++++++++++++")
    elif menu == 2:
        mult = num1 * num2
        print("****************************")
        print(mult)
        print("*****************************")
    elif menu == 3: 
        if num1>num2:
            maior = num1
        else:
            maior = num2
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(maior)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    elif menu == 4:
        num1 = int(input("Digite um valor: "))
        num2 = int(input("Digite um valor: "))
    menu = int(input("""Menu:
1 somar
2 multiplicar
3 maior
4 trocar numeros
5 sair do programa """))
