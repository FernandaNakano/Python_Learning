# Desafio 058
# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep
r = randint(0, 10)  # Faz o computador "pensar" em um número
#print(r)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)
acertou = False
t = 0
while not acertou:
    n = int(input('Em que número eu pensei? '))
    print('PROCESSANDO...')
    sleep(3)
    t += 1
    if r == n:
        acertou = True
    if r > n:
        print('Número incorreto, mais... tente novamente!')
    if r < n:
        print('Número incorreto, menos... tente novamente!')
if t == 1:
    print('Você acertou de primeira!!! O número é {}'.format(n))
else:
    print('Você acertou! O número é {}. Vc tentou {}x até acertar'.format(n, t))