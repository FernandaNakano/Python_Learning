# Desafio: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

v = list()
while True:
    valor = int(input('Digite um valor: '))
    if valor not in v:
        v.append(valor)
    cont = str(input('Deseja continuar? [sS]'))
    if cont in 'nN':
        break
v.sort()
print(f'Os números digitados foram: {v}')
