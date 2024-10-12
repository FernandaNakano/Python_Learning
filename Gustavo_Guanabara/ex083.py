# Desafio: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
pilha = []
e = (input('Digite uma expressão: '))
for s in e:
    if s == '(':
        pilha.append('()')
    elif s == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
        print('Sua expressão está váida!')
else:
        print('Sua expressão está inválida!')
