# Desafio #022
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

# Manipulação de texto:
# frase = 'Curso em Vídeo Python'

#            C u r s o   e m   V  í  d  e  o     P  y  t  h  o  n
#  Posição:  0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

# Fatiamento:
# frase[9] = V
# frase[9:13] = Víde    (o 13 ele não exibe, o último valor não entra)
# frase[9:21] = Vídeo Python
# frase[9:21:2] = VdoPto  (pula de 2 em 2)
# frase[:5] = Curso   (do início até a posição 5)
# frase[15:] = Python   (da posição 15 até o final)
# frase[9::3] = VePh

# len(frase) - 21 caracteres
# frase.count('o') - conta quantas letras o existem
# frase.count('o',0,13) - contas quantas letras "o" existem até a posição 12 (lembre-se que é 1 a menos)
# frase.upper().count('O') - Muda as letras o minúsculas e pocura por quantas letras O maiúsculas existem
# frase.find('deo') - vai retornar a posição 11, que é onde começou o 'deo' na string
# frase.find(' ') - vai retornar o número 5, que é a posição do primeiro espaço
# frase.find('Android') - retornará -1 que quer dizer que não foi encontrado
# 'Curso' in frase - retornará True que existe
# frase.replace('Python','Android') - troca a palavra por outra
# frase.upper() - troca para letras maiúsculas
# frase.lower() - troca para letras minúsculas
# frase.capitalize() - troca a string inteira para minúscula e somente o primeiro caracter para maiúscula
#                         Curso em vídeo Python
# frase.title() - troca a string inteira para minúscula e troca para maiúsculas a primeira letra das palavras depois do espaço
#                         Curso Em Vídeo Python

# frase.split() - cria uma divisão da string entre os espaços em branco, e refaz a indexação
#                 ['Curso', 'em', "Vídeo", 'Python']
#     Posição:        0       1      2         3

# >>> dividido = frase.split()
# >>> print(dividido)
# ['Curso', 'em', 'Video', 'Python']
# >>> print(dividido[0])
# Curso
# >>> print(dividido[2][3])     (pega a posição 2 que é "Vídeo" e ache a posição 3 que é "e")
# e


# '-'.join(frase) = Curso-em-Vídeo-Python   (troca o espaços em branco por traço)



# frase = '   Aprenda Python  '

#                  A p r e n d a     P  y  t  h  o  n
#  Posição:  0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18

# frase.strip() - remove os espaços em branco do começo e do final da string
# frase.rstrip() - remove os espaços em branco da direita da string
# frase.fstrip() - remove os espaços em branco da esquerda da string

# Desafio resolvido:

# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()

print('Seu nome em maiúsculas: {}'.format(nome.upper()))

print('Seu nome em minúsculas: {}'.format(nome.lower()))

print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))

d = nome.split()
pn = d[0]
print('Seu primeiro nome é {} e ele tem {} letras'.format(pn, len(pn)))
# ou usar o find para achar a posição do primeiro espaço em branco
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))