# Desafio: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

cad = []
cont = 's'
while cont in 'sS':

    n = input('Nome: ')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    cad.append([n, [n1, n2], media])

    cont = input('Quer continuar [s/n]? (default: s) ')

print('-=' * 30)
print(cad)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
i = 0
for i, l in enumerate(cad):
    print(f'{i+1:<4}{l[0]:<10}{l[2]:>8.1f}')
print('-' * 26)

cont2 = 0
while cont2 != 999:
    m = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if m == 999:
        break
    if m <= len(cad) - 1:
        print(f'Notas de {cad[m-1][0]} são {cad[m-1][1]}')

print('Volte sempre!')
