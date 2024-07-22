# Desafio 015
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

k = float(input('Qual a kilometragem percorrida? '))
d = int(input('Quantos dias de aluguel? '))
t = (d * 60) + (k * 0.25)

print('O total a ser pago é R${:.2f}.'.format(t))
