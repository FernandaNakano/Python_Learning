# Desafio 045
# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
r = randint(0, 2)  # Faz o computador "pensar" em um número
print(r)
print('O computador escolheu {}'.format(itens[r]))
print('''Suas opções:
      [ 0 ] PEDRA
      [ 1 ] PAPEL
      [ 2 ] TESOURA''')

j = int(input('Qual é a sua jogada? '))
#print('O jogador escolheu {}'.format(itens[j]))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')

if j != 0 and j != 1 and j != 2:
    print('Opção inválida. Tente novamente!')
elif j == r:
    print('EMPATOU!')
elif j > r and j + r == 1:
    print('Jogador ganhou!')
elif j < r and j + r == 2:
    print('Jogador ganhou!')
elif j > r and j + r == 3:
    print('Jogador ganhou!')
else:
    print('Computador ganhou!')
