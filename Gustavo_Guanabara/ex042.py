# Desafio 042
# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
# ESCALENO: todos os lados diferentes


l1 = float(input('Digite o primeiro segmento: '))
l2 = float(input('Digite o segundo segmento: '))
l3 = float(input('Digite o terceiro segmento: '))

if (l1 + l2 < l3) or (l1 + l3 < l2) or (l2 + l3 < l1):
    print('Com estes segmentos NÃO É POSSÍVEL formar um triângulo!')
else:
    print('OK, com estes segmentos é possível formar um triângulo ', end='')
    if l1 == l2 == l3:
        print('EQUILÁTERO!')
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print('ISÓCELES!')
    elif l1 != l2 != l3 != l1:
        print('ESCALENO!')