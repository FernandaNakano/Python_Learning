# Desafio: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

n = (int(input('Digite um número: ')),
        int(input('Digite outro número: ')),
        int(input('Digite mais um número: ')),
        int(input('Digite o último número: ')))

print(f'Você digitou os valores {n}')
if 9 in n:
    print(f'O valor 9 apareceu {n.count(9)} vezes')
else:
    print('O número 9 não foi digitado em nenhuma posição')

if 3 in n:
    print(f'O valor 3 foi digitado na {n.index(3)+1}a. posição')
else:
    print('O número 3 não foi digitado em nenhuma posição')

print(f'Os valores pares digitados foram: ', end='')
for c in n:
    if c % 2 == 0:
        print(c, end=' ')
print('\nFim')
