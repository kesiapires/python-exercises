#Faça um programa que tenha uma função notas() 
#que pode receber várias notas de alunos 
#e vai retornar um dicionário com as seguintes informações:

#– Quantidade de notas         
#– A maior nota                                                                                                                                            
#– A menor nota     
#– A média da turma                   
#– A situação (opcional)

#############  first try  ################
# def notas(*valores,sit=True): 
#     dict = {}
#     maior = 0
#     menor = 80000
#     dict.append(valores)
#     for i in dict:
#         if valores[i] < maior:
#             maior = valores[i]
#         if valores[i] > menor:
#             menor = valores[i]
#     media = float(sum(valores)/len(valores))
#     if media <= 4:
#         print(f'RUIM')
#     if media >= 7:
#         print("ÓTIMA")
#     if media in range(5,7):
#         print("MEDIANA")
#     return valores

def notas(*valRecebidos,sit=False):
    dict = {}
    dict['maior'] = 0
    dict['menor'] = 80000
    dict['media'] = 0
    for i in valRecebidos:
        if i > dict['maior']:
            dict['maior'] = i 
        if i < dict['menor']:
            dict['menor'] = i
    media = sum(valRecebidos)/len(valRecebidos)
    dict['media'] = media
    dict['total'] = len(valRecebidos)
    if sit == True:
        if dict['media'] <= 4:
            dict['situação'] = "RUIM"
        elif dict['media'] >=7:
            dict['situação'] = "EXCELENTE"
        elif dict['media'] > 5 and dict['media'] < 7:
            dict['situação'] = "MEDIANO"
    return dict
 
#main prog
resp = notas(3,6.9,9, sit=True)
print(resp)
  