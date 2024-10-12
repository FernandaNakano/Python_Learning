# Desafio 006
# Faça um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))

print('Analisando o número {}: \n o seu dobro é {} \n o seu tripo é {} \n e a raiz quadrada é {:.2f}'.format(n, (n*2), (n*3), (n**(1/2))))
# ou
print('Analisando o número {}: \n o seu dobro é {} \n o seu tripo é {} \n e a raiz quadrada é {:.2f}'.format(n, (n*2), (n*3), pow(n,(1/2))))
