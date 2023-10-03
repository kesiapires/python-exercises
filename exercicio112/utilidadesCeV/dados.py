def leiaDinheiro(mensagem):
    preco = str(input(mensagem)).strip().replace(",",".")
    while preco.isnumeric() is False:
        print(f'\033[04;033;40m ERRO! O valor {preco} é inválido.\033[m')
        preco = str(input(mensagem)).strip().replace(",",".")

    return float(preco)
    
    
