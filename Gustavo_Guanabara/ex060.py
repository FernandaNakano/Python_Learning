# Desafio 060
# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120
from math import factorial
n = int(input('Digite um número: '))
# f = factorial(n)
# ou
nm1 = n
f = 1
while nm1 > 0:
    print ('{}'.format(nm1), end='')
    print (' x ' if nm1 > 1 else ' = ', end='')
    f *= nm1
    nm1 -= 1
print('{}'.format(f))

