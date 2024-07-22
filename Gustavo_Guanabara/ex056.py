# Desafio 056
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.


mi = 0
si = 0
v = 0
nv = ""
mv = 0
for i in range(1, 5):
    print('----- {}a. pessoa -----'.format(i))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()

    si += idade
    mi = si / i
    if i == 1 and sexo in "Mm":
        v = idade
        nv = nome
    
    if idade > v and sexo in "Mm":
        v = idade
        nv = nome

    if sexo in "Ff" and idade < 20:
        mv += 1

print('A média da idade do grupo é: {}'.format(mi))
print('O nome do homem mais velho tem {} e se chama: {}'.format(v, nv))
print('A quantidade de mulheres com menos de 20 anos é: {}'.format(mv))
