# Lista dentro de lista:
# dados = ['Pedro', 25]
# pessoas = []
# pessoas.append(dados[:])

# pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
#            [   0     1 ]  [   0     1 ]  [   0     1 ]
#           [      0              1               2    ]

# print(pessoas[0][0])   # Pedro
# print(pessoas[1][1])   # 19
# print(pessoas[1])   # ['Maria', 19]

# teste = []
# teste.append('Gustavo')
# teste.append(40)
# galera = []
# galera.append(teste[:])
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste[:])
# print(galera)

# Resultado: [['Gustavo', 40], ['Maria'], 22]

# galera = [['João', 19], ['Ana', 33], ['joaquim', 13], ['Maria', 45]]
# for p in galera:
#     print(f'{p[0]} tem {p[1]} anos de idade')

# galera = []
# dado = []
# totmai = totmen = 0
# for c in range(0, 3):
#     dado.append(str(input('Nome: ')))
#     dado.append(str(input('Idade: ')))
#     galera.append(dado[:])
#     dado.clear()
# print(galera)

# for p in galera:
#     if p[1] >= 21:
#         print(f'{p[0]} é maior de idade.')
#         totomai += 1
#     else:
#         print(f'{p[0]} é menor de idade.')
#         totmen += 1
# print(f'Temos {totomai} maiores e {totmen} menores de idade.')

# Desafio: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

cont = 's'
maior = menor = 0
cad = []
geral = []
while cont in 'sS':
    cad = [str(input('Nome: ')), float(input('Idade: '))]

    if len(geral) == 0:
        maior = menor = cad[1]
    else:
        if cad[1] >= maior:
            maior = cad[1]
        if cad[1] < menor:
            menor = cad[1]

    geral.append(cad)
    print(f'Adicionado {cad} em {geral}')

    cont = input('Deseja continuar [sSnN]? ')
    # if cont in 'nN':
    #     break

print(f'Foram cadastradas {len(geral)} pessoas')

print(f'O maior peso foi de {maior}Kg. Pessoas: ', end='')
for p in geral:
    if p[1] == maior:
        print(f'{p[0]} ', end='')

print(f'\nO menor peso foi de {menor}Kg. Pessoas: ', end='')
for p in geral:
    if p[1] == menor:
        print(f'{p[0]} ', end='')

print('Fim')
