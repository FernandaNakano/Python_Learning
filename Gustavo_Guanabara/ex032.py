# Desafio #032
# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date
# from time import time
a = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))

if a == 0:
    a = date.today().year

if (a%4 == 0 and a%100 != 0) or a%400 == 0:
    print('O ano {} é BISSEXTO'.format(a))
else:
    print('O ano {} não é BISSEXTO'.format(a))