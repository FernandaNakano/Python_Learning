# Desafio: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

mylist = []
par = []
impar = []
cont = 's'

while True:
    v = int(input('Digite um número: '))
    mylist.append(v)

    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)

    cont = input('Deseja continuar [sSnN]? ')
    if cont in 'nN':
        break

print(f'A lista completa é {mylist}')
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')
