# Desafio 059
# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

print('-' * 20)
print('''Suas opções:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
print('-' * 20)

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

o = 0
while o != 5:
    o = int(input('Digite a opção desejada: '))
    
    if o == 1:
        r = n1 + n2
        print('A soma de {} com {} é igual a {}'.format(n1, n2, r))

    if o == 2:
        r = n1 + n2
        print('A multiplicação de {} com {} é igual a {}'.format(n1, n2, r))

    if o == 3:
        if n1 > n2:
            print('O maior número entre {} e {} é {}'.format(n1, n2, n1))
        elif n1 < n2:
            print('O maior número entre {} e {} é {}'.format(n1, n2, n2))
        elif n1 == n2:
            print('O primeiro número é igual ao segundo')

    if o == 4:
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))

    if o not in (1,2,3,4,5):
        print('Opção inválida, tente novamente!')

