#import math aqui pegamos todos as funções da biblioteca math.

from math import sqrt, floor, pow #Já aqui pegamos somente 3 funcionalidades,
#E não precisamos ultilizar a nomeção classica math.floor(),
#podemos somente colocar o nome da função e abrir os colchetes
#floor(num).

num = int(input('Digite um número: '))

raiz = sqrt(num)
potencia = pow(num, 2)


print('A raiz de {} é igual a {}.'.format(num, floor(raiz)))
print('A pótencia de {} sobre 2 é {}.'.format(num, potencia))