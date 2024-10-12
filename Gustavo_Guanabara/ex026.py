# Desafio #026
# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite a frase: ')).strip().upper()

print('A letra "A" aparece {} vezes na frase.'.format(frase.count('A')))

print('A letra "A" primeirmente na posição {} e por último na posição {}.'.format(frase.find('A')+1, frase.rfind('A')+1))