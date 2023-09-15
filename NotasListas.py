LISTAS

#listas são mutáveis


##############
CÓPIA
##############

Para fazer cópia de uma lista:  [:]
ex:
a = [4, 6, 3, 7]
b = a
#b[2] = 9
#alterando uma, altera a outra automaticamente pois n fiz cópia, mas uma ligação
sendo necessário fazer uma cópia da lista para alterar somente a cópia
ex:
b = a[:]
b[2] = 9



##############