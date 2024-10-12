# Desafio 036
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.


# if nome == 'Gustavo':
#     print('Que nome bonito')
# elif nome == 'Pedro' or nome == 'Maria':
#     print('Que nome popupar')
# elif nome in 'Ana Claudia Jessica Juliana':
#     print('Belo nome feminino')
# else:
#     print('Seu nome é bem normal')

c = float(input('Qual é o valor do imóvel? R$'))
s = float(input('Qual é o seu salário? R$'))
q = int(input('Em quantos anos vc vai pagar? '))

p = c / (q * 12)
m = s * 30 / 100

if p > m:
    print('O valor da prestação mensal que é de R${:.2f}, ultrapassa 30% do seu salário, que seria de R${:.2f}'.format(p, m))
else:
    print('Parabéns! A prestação mensal será de R${:.2f}'.format(p))
