#Desafio hipotenusa.

from math import hypot

catOposto = float(input('Digite o comprimento do cateto oposto: '))
catAdjacente = float(input('Digite o comprimento do cateto adjacente: '))

print('O comprimento da hipotenusa é {:.2f}.'.format(hypot(catOposto, catAdjacente)))
