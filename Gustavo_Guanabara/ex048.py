# Desafio 048
# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
t = 0
q = 0
for c in range(1, 501, 2):
    #print(c, end=' ')
    if c % 3 == 0:
        t += c
        q += 1
print('A soma de todos os {} é: {}'.format(q, t))
