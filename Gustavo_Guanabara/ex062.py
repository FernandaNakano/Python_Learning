# Desafio 062
# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

print('=' * 25)
print('{:^25}'.format('10 TERMOS DE UMA PA'))
print('=' * 25)

p = int(input('Primeiro termo: '))
r = int(input('Razão: '))

m = 1
g = 10
t = 1
while m != 0:
    while t <= g:
        print('{} - '.format(p), end='')
        p += r
        t += 1
    print('PAUSA')
    m = int(input('Quantos termos vc quer mostrar a mais? '))
    g += m
print('Progressão finalizada com {} termos mostrados'.format(g))

