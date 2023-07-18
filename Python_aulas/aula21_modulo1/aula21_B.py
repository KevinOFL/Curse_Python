# Aula 21 programa principal
# Vamos puxar o modulo de funções (aula21_A) que fizemos.

import aula21_A

num = int(input('Digite um número inteiro: '))
fac = aula21_A.fatorial(num)

print(f'''O fatorial de {num} é {fac}.
O dobro do fatorial {aula21_A.dobra(fac)}.
E o triplo é {aula21_A.triplo(fac)}.''')

