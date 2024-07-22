# Desafio 039
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
a = int(input('Qual seu ano de nascimento? '))

i = date.today().year - a

print('Quem nasceu em {} tem {} anos em {}'.format(a, i, date.today().year))

if i < 18:
    print('Ainda faltam {} anos para o alistamento\nSeu alistamento será em {}'.format(18 - i, (date.today().year + (18 - i))))
elif i > 18:
    print('Você já deveria ter se alistado há {} anos.\nSeu alistamento foi em {}'.format(i - 18, (date.today().year + (18 - i))))
else:
    print('Você tem que se alistar IMEDIATAMENTE')

