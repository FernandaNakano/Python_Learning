# Desafio 070
# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
t = pm = pb = v = 0
n = ''
while True:

    n = str(input('Produto: '))
    v = float(input('Valor (R$): '))

    if t == 0:
        tb = n
        pb = v

    t += v

    if v > 1000:
        pm += 1
    
    if v < pb:
        pb = v
        nb = n
        
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar [S/N]?: ')).strip().upper()[0]
    if cont == 'N':
        break
    
print(f'O total gasto na compra foi R${t:.2f}')
print(f'Há {pm} produto(s) que custa mais de R$1000')
print(f'E o produto mais barato foi: {nb}')
