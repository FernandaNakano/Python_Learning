# Desafio 068
# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
g = 0
while True:
    r = randint(0,10)
    # print(r)
    n = int(input('Digite um número: '))
    v = r + n
    parimp = v%2
    pi = ' '
    while pi not in 'PI':
        pi = str(input('Par ou impar? ')).upper().strip()[0]
    print(f'Vc jogou {n} e o computador {r}. Total de {v} ', end='')
    print('DEU PAR' if v%2 == 0 else 'DEU IMPAR')
    if pi == 'P':
        if parimp == 0:
            print("Você ganhou!")
            g += 1
        else:
            print("Você perdeu!")
            break
    elif pi == 'I':
        if parimp != 0:
            print("Você ganhou!")
            g += 1
        else:
            print("Você perdeu!")
            break
print(f'Game over!!! Vou venceu {g} vezes')
