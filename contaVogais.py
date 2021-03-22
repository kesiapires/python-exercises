s = input("Digite uma palavra: ")

contaVogal = 0
contaCons  = 0
for k in s:
	#if k == "a" or k == "e" or k == "i" or k == "o" or k == "u":
    if k in "aeiouAEIOU":
		contaVogal += 1
	else:
		contaCons += 1
	
print("A palavra ", s, " possui ", contaVogal, " vogais e ", contaCons, " consoantes")