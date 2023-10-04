def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError,TypeError):
            print('\033[4;31m ERRO. Por favor digite um numero inteiro válido!\033[m')
            continue
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError,TypeError):
            print('\033[4;31m ERRO. Por favor digite um numero real válido!\033[m')
            continue
        else:
            return n 