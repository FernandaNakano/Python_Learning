# Desafio 017
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import sqrt, hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

print('A hipotenusa vai medir {:.2f}'.format(sqrt(co ** 2 + ca ** 2)))

# ou usar a função hypot
print('A hipotenusa vai medir {:.2f}'.format(hypot(co, ca)))