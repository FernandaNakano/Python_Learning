# Desafio 065
# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

sn = 'S'
soma = m = c = 0
while sn != "N":
    n2 = int(input('Digite mais um número inteiro: '))
    if c == 0:
        maior = menor = n2
    soma = soma + n2
    if n2 > maior:
        maior = n2
    if n2 < menor:
        menor = n2
    sn = str(input('Continua [SsNn]: ')).upper().strip()[0]
    c += 1
m = soma / c
print('A média dos números digitados é: {}'.format(m))
print('O maior número foi: {}'.format(maior))
print('O menor número foi: {}'.format(menor))
