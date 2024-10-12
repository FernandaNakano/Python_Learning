# Desafio 064
# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

n = s = t =0
# s = int(input('Digite um número [999 para parar]: '))
while s != 999:
    s = int(input('Digite um número [999 para parar]: '))
    # ou colocar o if se não perguntar antes do while
    if s != 999:
        t += s
        n += 1
print('Houveram {} números e a soma deles é {}'.format(n, t))
