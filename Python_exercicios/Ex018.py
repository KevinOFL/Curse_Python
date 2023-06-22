#Desafio seno, coseno e tangente.

from math import sin, cos, tan, radians

angulo = int(input('Digite um ângulo: '))

print('O ângulo que você digitou {}º deu o valor de:\n{}\n seno: {:.2f}\n cosseno: {:.2f}\n tangente: {:.2f}\n{}'.format(angulo, ('-'*50), sin(radians(angulo)), cos(radians(angulo)), tan(radians(angulo)), ('-'*50)))