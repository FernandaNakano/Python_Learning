# Desafio 014
# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input('Qual é a temperatura em Celsius? '))

f = ((9 * c) / 5) + 32

print('A temperatura de {:.1f} graus em Celsius corresponde a {:.2f} graus em Fahrenheit.'.format(c, f))