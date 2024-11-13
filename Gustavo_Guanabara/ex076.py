# Desafio: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

p = ('arroz', 30.00,
     'feijão', 15.00,
      'açúcar', 4.00,
      'café', 6.00)

print('-' * 40)
print('LISTAGEM DE PREÇOS')
print('-' * 40)

# c = 0
# s = 1
# while c < len(p):
#     print(f'Produto{s}: {p[c]}, {p[c+1]}')
#     c += 2
#     s += 1

# ou

for pos in range(0, len(p)):
    if pos % 2 == 0:
        print(f'{p[pos]:.<30}', end=' ')
    else:
        print(f'R${p[pos]:>7.2f}')


print('Fim')
