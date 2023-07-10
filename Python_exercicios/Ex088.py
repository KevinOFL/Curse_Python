#Desafio  palpites mega sena.

from random import sample
from time import sleep

print('=-'*36)
print(' '*23, '\033[7;1m - Palpites Mega sena  - \033[m')
print('=-'*36)

todo = list()


while True:
    op = int(input('''Quantos jogos deseja sortear ?
-> '''))
    for contador in range (op):
        palpites = sample(range(1, 61), 6)

# Caso você não queira números repetidos no array inteiro use esse codigo de baixo junto do resto.
#
#       while palpites in todo:  # Verifica se os palpites já estão na lista todo
#           palpites = sample(range(1, 61), 6)
#       todo.append(palpites)
#
#       if len(todo) == op:  # Verifica se foram gerados o número solicitado de jogos
#           break

        todo.append(palpites)
    break

print('=-'*36)

print('>>'*2, f' Sorteando {op} palpites ', '<<'*2)
sleep(1.5)

for c, percorrer in enumerate(todo, start=1):
    print(f'Jogo {c}: {percorrer}')
    sleep(1)

print('=-'*36)





