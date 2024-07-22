# Desafio #027
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite o nome completo: ')).strip()
d = nome.split()
print('Seu primeiro nome é {} e seu último nome é {}.'.format(d[0], d[len(d)-1]))
