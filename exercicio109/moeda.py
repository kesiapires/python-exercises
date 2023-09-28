def dobro(valor, formato=False):
    dobro = valor + valor
    return dobro if not formato else moeda(dobro)

def metade(valor, formato=False):
    metade = valor/2
    return metade if formato is False else moeda(metade)


def aumentarPorcent(valor, formato=False):
    aumentarPorcent = valor + (valor/10)
    return aumentarPorcent if formato is False else moeda(aumentarPorcent)


def diminuirPorcent(valor, formato=False):
    diminuirPorcente = valor * 0.80
    return diminuirPorcente if formato is False else moeda(diminuirPorcente)



def moeda(valor):
   return 'R${:,.2f}'.format(valor)


