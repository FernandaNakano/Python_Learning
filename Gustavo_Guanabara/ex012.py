# Desafio 012
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input('Qual é o preço do produto? R$'))

d = p - (p * 5/100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% custará R${:.2f}'.format(p, d))