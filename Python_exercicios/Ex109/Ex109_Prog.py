# Desafio Trabalhando com modulos 2.

import Ex109_func
from Ex109_func import moeda

Ex109_func.apresentação()

n = float(input('Digite um número: R$'))
t = int(input('Digite a taxa: '))

Ex109_func.linha()

print(f'''              - - RESULTADO - -
Aumentamos {t}% do valor original {moeda(n)} -> {Ex109_func.aumentar(n, t, True)}
Diminuimos {t}% do valor original {moeda(n)} -> {Ex109_func.diminuir(n, t, True)}
Dobramos o valor original {moeda(n)} -> {Ex109_func.dobro(n, True)}
Dividimos o valor orinal {moeda(n)} -> {Ex109_func.metade(n, True)}''')

Ex109_func.linha()