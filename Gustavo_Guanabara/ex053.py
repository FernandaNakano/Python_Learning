# Desafio 053
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

f = str(input('Digite uma frase: ')).strip().replace(" ", "").upper()

# Para remover os espaços tb pode-se usar da forma abaixo, ao invés de usar o replace()
# palavras = f.split()
# junto = ''.join(palavras)

c = len(f)

fi = ""
for i in range(c-1, -1, -1):
    fi += f[i]
print(fi)

# Ao invés do for, pode-se usar:
# fi = f[::-1]

if f == fi:
    print('A frase É PALÍNDROMO!')
else:
    print('A frase NÃO É PALÍNDROMO!')
