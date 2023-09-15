frase = str(input("digite uma frase: ")).strip()
frase = frase.lower()
a =  frase.count("a")
ap = frase.find("a")
au = frase.rfind("a")
#au = frase.rfind("a")+1
print("Em {} encontramos {} letras a, sua primeira posição é {} e a ultima {}".format(frase,a,ap,au))
