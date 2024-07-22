# Desfio 049
# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

n = int(input('Digite um número para ver sua tabuada: '))

print('-' * 12)
for t in range(1, 11):
    print('{} x {:2} = {}'.format(n, t, (n*t)))
print('-' * 12)