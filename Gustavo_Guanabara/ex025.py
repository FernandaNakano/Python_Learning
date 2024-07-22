# Desafio #025
# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Qual é seu nome completo? ')).strip().upper()

print('Tem SILVA no nome? {}'.format('SILVA' in nome))