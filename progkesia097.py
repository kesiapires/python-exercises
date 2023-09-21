#Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), 
#que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.                                  
#Ex:    
# escreva(‘Olá, Mundo!’) Saída:                           
#~~~~~~~~~                                                    
#Olá, Mundo!                                                                                                                                                          
#~~~~~~~~~                                                     

def escreva(texto): 
    tamanhoTexto = len(texto)
    print('~'* tamanhoTexto+'\n'+ texto +'\n'+ '~'* tamanhoTexto)

escreva(str(input("Escreva um texto: ")))
