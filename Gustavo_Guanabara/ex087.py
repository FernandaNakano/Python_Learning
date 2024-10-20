# Desafio: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for  c in range(0, 3):
        m[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

s = tc = sl = 0
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{m[l][c]:^5}]', end='')
        if m[l][c] % 2 == 0:
            s = s + m[l][c]
        if c == 2:
            tc += m[l][c]
        if l == 1 and c == 0:
            sl = m[l][c]
        else:
            if l == 1 and m[l][c] >= sl:
                sl = m[l][c]
    print()

print(f'A soma dos valores pares é: {s}')
print(f'A soma dos valores da terceira coluna é: {tc}')
print(f'O maior valor da segunda linha é: {sl}')
