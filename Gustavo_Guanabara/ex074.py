# Desafio 074
# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

c = ""
cont= 0
while cont < 5:
    c += randint(0,20)
    print(c)
    cont += 1

