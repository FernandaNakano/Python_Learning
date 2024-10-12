# Desafio #019
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random
e = str(input('Digite o nome do aluno 1: '))
f = str(input('Digite o nome do aluno 2: '))
g = str(input('Digite o nome do aluno 3: '))
h = str(input('Digite o nome do aluno 4: '))

print('O aluno sorteado é o {}'.format(random.sample([e, f, g, h], k=1)))
# ou usando a função choice da classe random
print('O aluno sorteado é o {}'.format(random.choice([e, f, g, h])))
