

#Laços e range()
# range(0, 6) = 0 1 2 3 4 5
# range(1, 6) = 1 2 3 4 5
# range(1, 7) = 1 2 3 4 5 6
# range(0,7, 2) = 0 2 4 6
# range(6, 0) = 
# range(6, 0, -1) = 6 5 4 3 2 1
# range(6, 0, -2) = 6 4 2

# for c in range(6, 0, -2):
#     print(c)

# Desafio 046
# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('BOOOOMMM!!!!!!')