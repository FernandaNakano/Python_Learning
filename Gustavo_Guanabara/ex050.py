# Desafio 050
# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
t = 0
q = 0
for n in range(1, 7):
    r = int(input('Digite o número {}: '.format(n)))
    if r % 2 == 0:
        t += r
        q += 1
print('De todos os {} números, apenas {} são pares e a soma deles é: {}'.format(n, q, t))
