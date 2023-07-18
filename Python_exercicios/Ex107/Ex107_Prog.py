# Desafio Trabalhando com modulos.

import Ex107_func

Ex107_func.apresentação()

n = float(input('Digite um número: R$'))
t = int(input('Digite a taxa: '))

Ex107_func.linha()

print(f'''              - - RESULTADO - -
Aumentamos 25% do valor original R${n} -> R${Ex107_func.aumentar(n, t)}.
Diminuimos 35% do valor original R${n} -> R${Ex107_func.diminuir(n, t)}.
Dobramos o valor original R${n} -> R${Ex107_func.dobro(n)}.
Dividimos o valor orinal R${n} -> R${Ex107_func.metade(n)}.''')

Ex107_func.linha()