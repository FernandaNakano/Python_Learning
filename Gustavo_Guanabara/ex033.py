# Desafio #033
# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 > n2:
    if n1 > n3:
        print(n1)
else:
    if n2 > n3:
        print(n2)
    else:
        print(n3)

if n1 < n2:
    if n2 < n3:
        print(n1)
    else:
        print(n3)
else:
    if n2 < n3:
        print(n2)
    else:
        print(n3)

# ou
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('Maior: {}'.format(maior))

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('Menor: {}'.format(menor))
    