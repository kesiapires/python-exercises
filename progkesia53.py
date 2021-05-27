s = ""
word = str(input("Digite uma frase: ")).strip().lower()
for k in range (len(word)-1,-1,-1):
    s += word[k]
if word == s:
    print("A palavra {} é um palíndromo!".format(word))
else:
    print("A palavra {} não é um palíndromo.".format(word))