#crie um programa que leia varios numeros inteiros pelo teclado
#que no final mostre a media entre todos os numeros
#o maior e o menor
#o programa deve perguntar se o usuario que ou n continuar
s = 0
somanum = 0
media = 0
maior = 0
menor = 8000000000
simnao = "sim"
while simnao != "nao":
    num = int(input("Digite um valor: "))
    somanum = somanum+num
    #media = somanum/s
    if num>maior:
       maior = num
    if num<menor:
        menor = num
    s += 1
    simnao = str(input("Você quer continuar a digitar valores? ")).strip().lower()
print("A média entre os {} números é de {}. O maior valor é {}, e o menor é {}.".format(s,somanum/s,maior,menor))