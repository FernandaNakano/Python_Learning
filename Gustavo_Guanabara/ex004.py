# Desafio 004
# Faça um programa que leia algo no teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

# Primitive Types and Data Output
# int = 7  -4  0  9875
# float =  4.5  0.076  -15.223  7.0
# bool =  True False
# str = 'Olá'  '7.5'   ''

# Verificar o tipo de uma variável:
# print(type(n1))

# Verificar se é alfa-numérico:
# print(n1.isalpha())
# O resultado será True ou False

n = input('Digite um valor: ')

print('O tipo primitivo deste valor é:', type(n))
print('É maiúsculo?', n.isupper())
print('É minúsculo?', n.islower())
print('Só tem espaço?', n.isspace())
print('É número?', n.isnumeric())
print('É alfabético?', n.isalpha())
print('É alfanumérico?', n.isascii())
print('Está capitalizada?', n.istitle())