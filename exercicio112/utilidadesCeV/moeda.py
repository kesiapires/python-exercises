def dobro(valor, formato=False):
    dobro = valor + valor
    return dobro if not formato else moeda(dobro)

def metade(valor, formato=False):
    metade = valor/2
    return metade if formato is False else moeda(metade)


def aumentarPorcent(valor,porcentaum, formato=False):
    aumentarPorcent = valor + (valor*porcentaum)/100
    return aumentarPorcent if formato is False else moeda(aumentarPorcent)


def diminuirPorcent(valor, porcentdim, formato=False):
    diminuirPorcente = valor * (100-porcentdim)/100
    return diminuirPorcente if formato is False else moeda(diminuirPorcente)


def moeda(valor):
   return 'R${:,.2f}'.format(valor)


def resumo(valor, porcentdim, porcentaum):
    print('-'*25)
    print(f'Preço analisado: {valor}')
    print(f'Metade do preço: {metade(valor, True)}')
    print(f'Dobro do preço: {dobro(valor, True)}')
    print(f'{porcentaum} de aumento: {aumentarPorcent(valor,porcentaum, True)}')
    print(f'{porcentdim} de redução: {diminuirPorcent(valor,porcentdim, True)}') 
    print('-'*25)





