# Cores - padrão ANSI

# Style: 
# 0 none
# 1 bold
# 4 underline
# 7 negative

# Text / back:
# 30 / 40 branco
# 31 / 41 vermelho
# 32 / 42 verde
# 33 / 43 amarelo
# 34 / 44 azul
# 35 / 45 roxo
# 36 / 46 azul claro
# 37 / 47 cinza

# Exemplo:
# \033[<style>;<text>;<back>m
# \033[0;33;44m

# \033[m  - desfaz as alterações

print('\033[0;31;43mOlá, mundo!\033[m')
# ou
nome = 'Fernanda'
print('Olá, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))
# ou usando dicionário
cores = {'limpa':'\033[m',
          'azul':'\033[34m',
          'amarelo':'\033[33m',
          'pretoebranco':'\033[7;30m'}
print('Olá, {}{}{}!!!'.format(cores['amarelo'], nome, cores['limpa']))
