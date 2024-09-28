# Desafio 069
# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

cont = 'S'
ti = tm = tf = 0
while True:
    n = str(input('Nome: ')).strip()
    i = int(input('Idade: '))
    s = ' '
    while s not in 'MF':
        s = str(input('Sexo [M/F]: ')).strip().upper()

    if i > 18:
        ti += 1

    if s == 'M':
        tm += 1
    
    if s == 'F' and i < 20:
        tf += 1
    
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    if cont == 'N':
        break

print(f'Há {ti} pessoas maiores de 18 anos')
print(f'Há {tm} homens cadastrados')
print(f'Há {tf} mulheres menores de 20 anos')




