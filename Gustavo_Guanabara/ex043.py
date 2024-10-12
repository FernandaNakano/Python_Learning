# Desafio 043
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# IMC abaixo de 18,5: Abaixo do Peso
# Entre 18,5 e 25: Peso Ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida

p = float(input('Digite seu peso em quilos: '))
a = float(input('Digite sua altura em metros: '))

imc = p / (a ** 2)

print('O IMC desta pessoa é {:.1f}'.format(imc))
if imc <= 18.5:
    print('Você está na faixa de ABAIXO DO PESO NORMAL')
elif imc <= 25:
    print('PARABÉNS, você está na faixa de PESO IDEAL')
elif imc <= 30:
    print('Você está na faixa de SOBREPESO')
elif imc <= 40:
    print('Você está na faixa de OBESIDADE')
else:
    print('Você está na faixa de OBESIDADE MÓRBIDA')
