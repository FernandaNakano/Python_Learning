# Desafio #035
# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

l1 = float(input('Digite o primeiro segmento: '))
l2 = float(input('Digite o segundo segmento: '))
l3 = float(input('Digite o terceiro segmento: '))

if (l1 + l2 < l3) or (l1 + l3 < l2) or (l2 + l3 < l1):
    print('Com estes segmentos NÃO É POSSÍVEL formar um triângulo!')
else:
    print('OK, com estes segmento é possível formar um triângulo!')


