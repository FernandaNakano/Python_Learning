# Desafio: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

# mylist = []
# for c in range(0, 5):
#     v = int(input('Digite um valor: '))
#     if c == 0 or v > mylist[-1]:
#         mylist.append(v)
#     else:
#         cont = 0
#         for c2 in range(0, len(mylist)):
#             if v <= mylist[c2] and cont == 0:
#                 mylist.insert(c2, v)
#                 cont = 1
#         print(mylist)
# or

mylist = []
for c in range(0, 5):
    v = int(input('Digite um valor: '))
    if c == 0 or v > mylist[-1]:
        mylist.append(v)
    else:
        c2 = 0
        while c2 < len(mylist):
            if v <= mylist[c2]:
                mylist.insert(c2, v)
                break
            c2 += 1
        print(mylist)
print('Fim')
