# Desafio #016
# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira

# Módulos - bibliotecas
# import <biblioteca_inteira>  ou
# from <bibioteca> import <função>, <função> 

# import math
# usar math.floor()

# from math import sqrt,floor
# usar floor()

# funções da biblioteca math: ceil (arredonda para cima), floor (arredonda para baixo), trunc, pow, sqrt (raiz quadrada), factorial

# Mostrar todos as bibliotecas a serem instaladas:
# import <clicar em CTRL+espaço>

# Desafio resolvido:
from math import trunc

n = float(input('Digite um valor: '))
print('O número {} tem a parte Inteira {}'.format(n, trunc(n)))
# ou usar a função int() o qual já é carregada por default.
print('O número {} tem a parte Inteira {}'.format(n, int(n)))
