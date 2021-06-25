#fatorial de um numero usando while
num = int(input("Digite um número: "))
fat = num
original = num
while num != 1:
    num = num - 1
    fat = fat * num
print("O fatorial do número {} é {}".format(original,fat))

#fatorial de um numero usando for
num = int(input("Digite um número: "))
fat = num
for i in range (1, num):
    fat = fat * i
print("O fatorial do número {} é {}".format(num,fat))