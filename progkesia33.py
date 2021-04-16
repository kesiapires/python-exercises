num0 = float(input("digite um numero: "))
num1 = float(input("digite um numero: "))
num2 = float(input("digite um numero: "))
if num0 >= num1 and num0 >= num2:
       print("o maior numero é", num0 )
elif num1 >= num0 and num1 >= num2:
       print("o maior numero é", num1 )
elif num2 >= num1 and num2 >= num0:
       print("o maior numero é", num2)

if num0 <= num1 and num0 <= num2:
       print("o menor numero é", num0 )
elif num1 <= num0 and num1 <= num2:
       print("o menor numero é", num1 )
elif num2 <= num1 and num2 <= num0:
       print("o menor numero é", num2)
   # outra forma de fazer
#menor = a
#if b<c or b<a
#       menor = b
#if c<b or c<a
#       menor = c
#maior = a
#if b>c or b>a
#       maior = b
#if c>b or c>a       
#       maior = c
#print("O menor numero é", menor)
#print("O maior numero é", maior)