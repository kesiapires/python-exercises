def dobro(valor, formato=False):
    dobro = valor + valor
    return dobro if not formato else moeda(dobro)

def metade(valor, formato=False):
    metade = valor/2
    return metade if formato is False else moeda(metade)


def aumentarPorcent(valor,porcent, formato=False):
    aumentarPorcent = valor + (valor/porcent)
    return aumentarPorcent if formato is False else moeda(aumentarPorcent)


def diminuirPorcent(valor, porcent, formato=False):
    diminuirPorcente = valor * (100-porcent)/100
    return diminuirPorcente if formato is False else moeda(diminuirPorcente)



def moeda(valor):
   return 'R${:,.2f}'.format(valor)


