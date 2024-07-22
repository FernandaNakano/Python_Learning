# Desafio 011
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m2.


l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))

area = l * a

print('Sua parede tem a dimensão de {:.2f}x{:.2f} e sua área é de {:.3f}m2.'.format(l, a, area))
print('Para pintar esta parede, você precisará de {:.4f}l de tinta'.format(area/2))