# Desafio 074
# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

n = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print(f'Os números sorteados foram: {n}')
s = sorted(n)
menor = s[0]
print(f'O menor número é: {menor} ')
print(f'O menor número é: {min(n)} ')
maior = s[len(s)-1]
[print(f'O maior número é: {maior}')]
[print(f'O maior número é: {max(n)}')]
