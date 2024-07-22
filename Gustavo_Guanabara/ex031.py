# Desafio #031
#  Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

v = float(input('Qual é a distância da sua viagem em Km/h? '))

if v > 200:
    vt = v * 0.45
else:
    vt = v * 0.5
# ou
vt = v * 0.5 if v <= 200 else v * 0.45

print('O preço da sua passagem será de R${:.2f}'.format((vt)))
