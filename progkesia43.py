#calculando o imc
peso = float(input("Qual o seu peso? "))
altura = float(input("Qual a sua altura? "))
calculo = (peso)/altura**2
if calculo <= 18.5 :
    print("Você está abaixo do peso.")
elif calculo <= 24.9 :
    print(" Você está no seu peso ideal.")
elif calculo <= 29.9 :
    print("Você está acima do peso.")
elif calculo <= 40 :
    print("Você está obeso.")
else :
    print("Você está obeso mórbido.")