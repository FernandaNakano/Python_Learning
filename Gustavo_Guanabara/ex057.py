# Desafio 057
# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
s = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]

while s not in 'MF':
    s = str(input('Campo inválido. Digite M ou F: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(s))

