# Desafio 071
# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#  OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
v = int(input('Digite o valor a ser sacado (R$): '))
# c = c1 = c10 = c20 = c50 = 0
# while c == 0:
#     if v >= 50:
#         c50 = v // 50
#         if v % 50 == 0:
#             c = 1
#         else:
#             v = v % 50
#     elif v >= 20:
#         c20 = v // 20
#         if v % 20 == 0:
#             c = 1
#         else:
#             v = v % 20
#     elif v >= 10:
#         c10 = v // 10
#         if v % 10 == 0:
#             c = 1
#         else:
#             v = v % 10
#     elif v >= 1:
#         c1 = v // 1
#         if v % 1 == 0:
#             c = 1
#         else:
#             v = v % 1
# print(f'Vc receberá:\n{c1} notas de R$1\n{c10} notas de R$10\n{c20} notas de R$20\n{c50} notas de R$50')

# ou

total = v
ced = 50
c = 0
while True:
    if total >= ced:
        total -= ced
        c += 1
    else:
        if c > 0:
            print(f'Total de {c} cédulas de {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        c = 0
        if total == 0:
            break
        