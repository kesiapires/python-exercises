#contagem regressiva de 10 a 0, com pausa de 1 segundo entre a contagem
import time
for k in range (10,0,-1):
    time.sleep(1)
    print("Fogos em: ",k)
print("BLOOM!!!!!!")