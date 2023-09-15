km = float(input("Qual a distância da viagem? "))
v1 = (km*0.50)
v2 = (km*0.45)
if km > 200:
    print("sua viagem sairá por: {}".format(v2))
elif km <= 200:
    print("sua viagem sairá por: {}".format(v1))