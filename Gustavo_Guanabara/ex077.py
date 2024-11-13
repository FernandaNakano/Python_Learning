# Desafio: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

p = ('banana',
     'abacaxi',
     'morango',
     'pera',
     'jabuticaba')

for palavra in p:
    print(f'Na palavra {palavra.upper()} temos', end=' ')
    for vogal in palavra:
        if vogal.lower() in 'aeiou':
            print(f'{vogal}', end=' ')
    print('')
