# Desafio 008
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n = float(input('Uma distância em metros: '))

print('A medida de {}m corresponde a \n{:.3f}km \n{:.2f}hm \n{:.1f}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(n, (n*0.001), (n*0.01), (n*0.1), n*10, n*100, n*1000))
