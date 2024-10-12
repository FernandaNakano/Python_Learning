
# Tuplas
# lanche = ('hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

# for comida in lanche:
#     print(f'Eu vou comer {comida}')

# for cont in range(0, len(lanche)):
#     print(f'Eu vou comer {lanche[cont]} na posição {cont}')

# for pos, comida in enumerate(lanche):
#     print(f'Eu vou comer {comida} na posição {pos}')

# print(sorted(lanche))

# () = tupla
# [] = lista

# a = (2, 5, 4)
# b = (5, 8, 1, 2)
# c = b + a   # (5, 8, 1, 2, 2, 5, 4)
# print(len(c))    # 7
# print(c.count(5)) # 2 - existem dois números 5
# print(c.index(5)) # 0 - o número cinco está na posiçao 0
# print(c.index(5, 1)) # 5 - o número cinco, depois da posição 1, está na posiçao 5
# print('Comi pra caramba')

# Desafio 072
# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

extenso = ('zero', 'um', 'dois', 'tres', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')
while True:
    n = int(input('Digite um número de 0 a 20: '))
    if 0 <= n <= 20:
        print(f'O número foi: {extenso[n]}')
        cont = ' '
        while cont not in 'SN':
            cont = str(input('Deseja continuar? [S/N]? ')).strip().upper()[0]
        if cont == 'N':
            break
    else:
        print('Tente novamente.')

