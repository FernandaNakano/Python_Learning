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
