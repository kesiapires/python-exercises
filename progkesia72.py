#tuplas
#usando tuplas para devolver o valor por extenso

numeroext = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

while True:
    num = int(input("Digite um numero entre 0 e 20: "))
    #if num <= 0 or num >20:
    #    break
    #print(" Digite novamente :)") #, end=''    
    valor = numeroext[num]
    print(f"Você digitou o numero {valor}")
    break