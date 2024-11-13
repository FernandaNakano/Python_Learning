# Desafio: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.


mylist = []
cont = 's'
while cont in 'sS':
    mylist.append(int(input('Digite um valor: ')))

    cont = input('Deseja continuar [sSnN]? ')

print(f'Foram digitados {len(mylist)} elementos')

mylist.sort(reverse=True)
print(f'Os valores em ordem descrescente são: {mylist}')

if 5 in mylist:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 não está na lista!')
