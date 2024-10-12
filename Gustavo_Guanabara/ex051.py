# Desafio 051
# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('=' * 25)
print('{:^25}'.format('10 TERMOS DE UMA PA'))
print('=' * 25)

p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = p + (10 - 1) * r

for c in range(p, d+1, r):
    print(c, end=' - ')
print('ACABOU')
