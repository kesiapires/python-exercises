##Crie um programa que leia nome,
#ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
#Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação 
#e o salário. 
#Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

dados = {}
from datetime import datetime
dados['nome'] = str(input("Digite seu nome: "))
anoNascimento = int(input("Digite o seu ano de nascimento: "))
dados['idade'] = datetime.now().year - anoNascimento
dados['ctps'] = int(input("Carteira de trabalho: (0 = não tem): "))
if dados['ctps'] != 0:
    dados['anoContratacao'] = int(input("Digite o ano de contratação: "))
    dados['salario'] = int(input("Digite o seu salário: "))
    dados['aposentadoria'] = dados['idade'] + ((dados['anoContratacao'] + 35) - datetime.now().year)
print("IXXI" *30)
for k,v in dados.items():
    print(f'  * {k} = {v}')