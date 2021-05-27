#caalculando a média
nota1 = float(input("Digite o valor da primeira nota: "))
nota2 = float(input("Digite o valor da segunda nota: "))
media = (nota1+nota2)/2
if media < 5 :
    print("Você foi reprovado.")
elif media >= 5 and media < 7 :
    print("Você está de recuperação.")
elif media >= 7 :
    print("Parabens, você foi aprovado!!!!!")