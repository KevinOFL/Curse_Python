#Aula sobre como ultilizar a função break nos laços condicionais.

import math

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n

print('A soma vale {}'.format(s))

#F strings

print(f'A soma vale {s}')

nome = 'Kevin'
idade = 18
salario = 1801.90

print(f'O {nome} tem {idade} anos e ganhou 10% de aumento de salário R${math.floor(salario + (salario * 0.10))}')