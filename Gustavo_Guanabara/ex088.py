# Desafio: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

# from random import sample
# nj = int(input('Quantos jogos você quer que eu sorteie? '))

# j = []
# for c in range(0, nj):
#     n = sample(range(1, 60), 6)
#     n.sort()
#     j.append(n)
#     print(f'Jogo {c+1}: {n}')
#     j.clear()

# ou

from random import randint
from time import sleep
lista = []
jogos = []
print('-' * 30)
print(f' JOGA NA MEGA SENA ')
print('-' * 30)
nj = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= nj:
    c = 0
    while True:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
            c += 1
        if c >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f' SORTEANDO {nj} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
