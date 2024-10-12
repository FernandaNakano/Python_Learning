# Desafio 005
# Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e o seu antecessor

# Operações Aritméticas
# + adição
# - subtração
# + multiplicação
# / divisão
# ** potência   9**2  ou pow(9,2)   raiz quadrada de 81 é igual a 81**(1/2) que resulta em 9.0     print('='*5) que resulta =====
# // divisão inteira - exemplo: 5//2  = 2
# % resto da divisão - exemplo: 5%2  =  1

# Ordem de Precedência
# 1 - ()
# 2 - **
# 3 - * / // %
# 4 - + -

# Alinhamento

nome = input('Qual é seu nome? ')
print('Prazer em te conhecer, {}!'.format(nome))
# Prazer em te conhecer, Fernanda!
print('Prazer em te conhecer, {:20}!'.format(nome))
# Prazer em te conhecer, Fernanda            !
print('Prazer em te conhecer, {:>20}!'.format(nome))
# Prazer em te conhecer,             Fernanda!
print('Prazer em te conhecer, {:^20}!'.format(nome))
# Prazer em te conhecer,       Fernanda      !
print('Prazer em te conhecer, {:=^20}!'.format(nome))
# Prazer em te conhecer, ======Fernanda======!

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A some é {}, \n o produto é {} e \n a divisão é {}'.format(s, m, d), end=' >>>')
print('Divisão inteira {} e potência {}'.format(di, e))
# Digite um valor: 3
# Digite outro valor: 2
# A some é 5, 
#  o produto é 6 e
#  a divisão é 1.5 >>>Divisão inteira 1 e potência 9

# Resolução do desafio:
n = int(input('Digite um valor: '))
s = n + 1
a = n - 1
print('Seu sucessor é {} e seu antecessor é {}'.format(s, a))

# Outra forma mas usando menos variáveis
print('Analisando o valor {}, seu antecessor é {} e o seu sucessor é {}'.format(n, (n-1), (n+1)))