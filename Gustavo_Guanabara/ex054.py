# Desafio 054
# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

mm = 0
nm = 0
for n in range(1, 8):
    d = int(input('Digite o ano de nascimento da pessoa {}: '.format(n)))
    m = date.today().year - d
    if m < 18:
        print('Ainda não é maior')
        nm += 1
    else:
        print('Já é maior')
        mm += 1

print('{} pessoas já são maiores de 18 e {} pessoas ainda não são.'.format(mm, nm))
    


