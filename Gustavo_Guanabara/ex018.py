# Desafio #018
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, cos, tan, sin
a = float(input('Digite um ângulo: '))

print('Seno: {:.2f} \nCosseno: {:.2f} \nTangente: {:.2f}'.format(sin(radians(a)), cos(radians(a)), tan(radians(a))))
