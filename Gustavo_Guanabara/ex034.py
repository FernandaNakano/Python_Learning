# Desafio #034
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

p = float(input('Qual é o salário do funcionário? R$'))

a = 15
if p > 1250:
    a = 10

d = p + (p * a / 100)
print('Um funcionário que ganhava R${:.2f}, com {}% de aumento, passa a receber R${:.2f}'.format(p, a, d))