# Desafio 055
# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

m = 0
n = 0
for n in range(1, 6):
    p = float(input('Digite o peso da {}a. pessoa: '.format(n)))
    if n == 1:
        m = p
        n = p
    else: 
        if p > m:
            m = p

        if p < n :
            n = p

print('{} foi o maior peso e {} foi o menor peso.'.format(m, n))
