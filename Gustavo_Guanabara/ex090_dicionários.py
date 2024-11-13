
# dados = {}  ou dados = dict()
# dados = {'nome':'Pedro','idade':25}
# dados['sexo']='M'  # insere mais um índice e conteúdo

# { 'Pedro', 25, 'M'}
#    nome    idade sexo -> o índice/key é agora "nome" e idade
#      0       1    -> o índice/key não é mais 0, 1, etc

# print(dados['nome'])  # Pedro
# print(dados['idade']) # 25

# del dados['idade']

# Exemplo:

# filme
# { 'Star Wars', 1977, 'George Lucas'}
#    titulo      ano    diretor

# print(filme.values())   # 'Star Wars', 1977, 'George Lucas'
# print(filme.keys())     # 'titulo', ano, 'diretor'
# print(filme.items())    # imprime os keys e os values

# for k, v in filme.items():
#    print(f'O key {k} é value {v}')

# O key titulo é value Star Wars
# O key ano é value 1977
# O key diretor é value George Lucas

# Pode-se ter dicionário dentro de lista e vice-versa

# No script:
# pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
# print(f'O {pessoas["nome"]} tem {["idade"]} anos.')

# estado = {}
# brasil = []
# for c in range(0, 3):
#     estado['uf'] = str(input('Unidade Federativa: '))
#     estado['sigla'] = str(input('Sigla do Estado: '))
#     brasil.append(estado.copy())
#     print(brasil)
# for e in brasil:
#     for v in e.values():
#         print(v, end=' ')
#     print()

# Desafio:

cad = {}

cad['nome'] = input('Nome: ')
cad['media'] = float(input(f'Média de {cad["nome"]}: '))

print(f'Nome é igual a {cad["nome"]}')
print(f'Média é igual a {cad["media"]}')
if cad["media"] < 7:
    print(f'Situação é igual a reprovado')
else:
    print(f'Situação é igual a aprovado')
