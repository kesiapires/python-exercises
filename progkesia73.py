#tabela do brasileirão usando tuplas
#20/08/2021

tabelabra = ("Atlético mineiro", "Palmeiras", "Fortaleza", "Bragantino", "Flamengo", "Atlético-PR", "Atlético Goianense", "Ceará", "Internacional", "Santos", "Corinthians", "Jentude", "Bahia", "São Paulo", "Fluminense", "Cuiabá", "Sport Recife", "América-MG", "Grêmio", "Chapecoense")
print(f"""os 5 primeiros colocados são:
{tabelabra[0:5]}
Os 4 ultimos colocados são: 
{tabelabra[-5:]}
A lista do time em ordem alfabetica é: 
{sorted(tabelabra)}
A chapecoense está na posição: 
""")
#{tabelabra.index("chapecoense")}""")