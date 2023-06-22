#Desafio seno, coseno e tangente.

from math import sin, cos, tan

angulo = int(input('Digite um ângulo: '))

print('O ângulo que você digitou {}º deu o valor de:\n{}\n seno: {}\n cosseno: {}\n tangente: {}\n{}'.format(angulo, ('-'*50), sin(angulo), cos(angulo), tan(angulo), ('-'*50)))