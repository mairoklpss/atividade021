# Crie um programa que faça uma contagem regressiva de 10 até 0 e exiba "FIM!" ao final.
from time import sleep
for contador in range(10, -1, -1): 
    print (contador)
    sleep(0.5)
print("FIM!")