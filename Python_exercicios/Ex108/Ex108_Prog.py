# Desafio Trabalhando com modulos 2.

import Ex108_func
from Ex108_func import moeda

Ex108_func.apresentação()

n = float(input('Digite um número: R$'))
t = int(input('Digite a taxa: '))

Ex108_func.linha()

print(f'''              - - RESULTADO - -
Aumentamos {t}% do valor original {moeda(n)} -> {moeda(Ex108_func.aumentar(n, t))}.
Diminuimos {t}% do valor original {moeda(n)} -> {moeda(Ex108_func.diminuir(n, t))}.
Dobramos o valor original {moeda(n)} -> {moeda(Ex108_func.dobro(n))}.
Dividimos o valor orinal {moeda(n)} -> {moeda(Ex108_func.metade(n))}.''')

Ex108_func.linha()