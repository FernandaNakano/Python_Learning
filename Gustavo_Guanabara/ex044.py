# Desafio 044
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# 2x no cartão: preço formal 
# 3x ou mais no cartão: 20% de juros

print('{:=^40}'.format(' LOJAS GUANABARA '))
v = float(input('Digite o valor do produto: '))
print('''Formas de pagamento:
        [ 1 ] à vista dinheiro/cheque: 10% de desconto
        [ 2 ] à vista no cartão: 5% de desconto
        [ 3 ] 2X no cartão: preço formal
        [ 4 ] 3X ou mais no cartão: 20% de juros''')
c = int(input('Digite a opção de pagamento: '))

if c == 1:
    vt = v - (v * 10 / 100)
    print('Sua compra de R${:.2f} vai custar R${} no final'.format(v, vt))
elif c == 2:
    vt = v - (v * 5 / 100)
    print('Sua compra de R${:.2f} vai custar R${} no final'.format(v, vt))
elif c == 3:
    vt = v + (v * 0 / 100)
    vp = vt / 2
    print('Sua compra de R${:.2f} SEM JUROS vai custar R${:.2f} em 2 parcelas de R${:.2f}'.format(v, vt, vp))
elif c == 4:
    p = int(input('Quantas parcelas? '))
    if p < 3:
        print('O número de parcelas precisa ser maior ou igual a 3')
    else:
        vt = v + (v * 20 / 100)
        vp = vt / p
        print('Sua compra de R${:.2f} vai custar R${:.2f} com JUROS. Serão {} parcelas de R${:.2f}'.format(v, vt, p, vp))
else:
    print('Opção inválida. Tente novamente!')