# Desafio #028
# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
r = randint(0, 5)  # Faz o computador "pensar" em um número
# print(r)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
n = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
print('Você acertou!' if r == n else 'GANHEI! Eu pensei no número {} e não no {}!'.format(r,n))
# ou
if r == n:
    print('Você acertou!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(r,n))