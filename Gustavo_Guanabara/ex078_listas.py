
# Listas
# lanche = ['sanduiche', 'suco', 'pizza', 'pudim']
#                0          1       2        3

# lanche[3] = 'picole'  # substitui o conteúdo da posição 3
# lanche.append('biscoito')  # adicionado no final na posição 4
# lanche.insert(0,'cachorro-quente')  # insere na posição 0, mudando a posição dos demais itens para a direita

# del lanche[3]  # comando del para remover o item na posição 3 e reposiciona o índice
# lanche.pop(3)  # normalmente usa-se para remover o último item, mas se passar o parâmetro apaga o item desejado e reposiciona o índice
# lanche.remove('pizza') # remove o primeiro item desejado e reposiciona o índice. Se tentar remover algo que não existe, mostra erro.

# valores=list(range(4, 11))   # cria lista de 4 a 10
# valores.sort(reverse=True)  # ordem reversa
# len(valores)  # o resultado é 7

# for c, v in enumerate(lanche):
#         print(f'Na psoção {c} encontrei o valor {v}!')

# Ligação de listas
# a = [2, 3, 4, 7]
# b = a # Faz uma ligação entre as listas, então a e b terão o mesmo conteúdo ao executar o comando 'b[2] = 8'
# b = a[:] # Faz uma cópia, então o conteúdo das listas será diferente quando executada o comando abaixo
# b[2] = 8
# print(f'Lista A: {a}')
# print(f'Lista B: {b}')

# Desafio: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

v = []
for c in range(0, 5):
    v.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = v[c]
    else:
        if v[c] > maior:
            maior = v[c]
        if v[c] < menor:
            menor = v[c]

print(f'Vc digitou os valores {v}')

print(f'O maior valor digitado foi {maior} nas posições ', end='')
for p, n in enumerate(v):
    if n == maior:
        print(f'{p}... ', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for p, n in enumerate(v):
    if n == menor:
        print(f'{p}... ', end='')
print()
