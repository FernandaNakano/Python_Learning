# Desafio #020
# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random  
e = str(input('Digite o nome do aluno 1: '))
f = str(input('Digite o nome do aluno 2: '))
g = str(input('Digite o nome do aluno 3: '))
h = str(input('Digite o nome do aluno 4: '))

print('A ordem de apresentação será: {}'.format(random.sample([e, f, g, h], k=4)))
# ou usando a função shuffle da classe random
lista = [e, f, g, h]
random.shuffle(lista)
print('A ordem de apresentação será:', lista)
