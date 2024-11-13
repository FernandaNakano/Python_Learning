# Desafio: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

vl = [[], []]
v = 0
for s in range(1, 8):
    v = int(input(f"Digite o {s}o. valor: "))

    if v % 2 == 0:
        vl[0].append(v)
    else:
        vl[1].append(v)

vl[0].sort()
vl[1].sort()
print(f'Os valores pares digitados foram: {vl[0]}')
print(f'Os valores ímpares digitados foram: {vl[1]}')
