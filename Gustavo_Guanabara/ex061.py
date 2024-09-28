# Desafio 061
# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('=' * 25)
print('{:^25}'.format('10 TERMOS DE UMA PA'))
print('=' * 25)

p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
# d = p + (10 - 1) * r

# for c in range(p, d+1, r):
#     print(c, end=' - ')
# print('ACABOU')

t = 1
while t <= 10:
    print(p, end=' - ')
    p += r
    t += 1
print('ACABOU')