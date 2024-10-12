# Desafio 063
# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8

n = int(input('Quantos termos vc quer mostrar: '))
c = 3
f = 0
a = 1
print('{} - {} - '.format(f, a), end='')
while c <= n:
    g = f + a
    print('{} - '.format(g), end='')
    f = a
    a = g
    c += 1
print('FIM')
