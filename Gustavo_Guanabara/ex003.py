# Desafio 003
# Crie um programa que leia dois números e mostre a soma entre eles

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

n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
s = n1 + n2
print('A soma vale:', s)
print('A soma vale: {}'.format(s))
print('A soma entre', n1, 'e', n2, 'vale:', s)
print('A soma entre {} e {} vale: {}'.format(n1,n2,s))

