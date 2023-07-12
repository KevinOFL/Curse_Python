#Desafio 4 dados.

from random import randint
from time import sleep

print('=-'*36)
print(' '*27, '\033[7;1m - 4 Dados  - \033[m')
print('=-'*36)

jogadores = {'Jogador 1': randint(1, 6), 'Jogador 2': randint(1, 6),
'Jogador 3': randint(1, 6), 'Jogador 4': randint(1, 6)}

print(' OS jogadores estão jogando...')
sleep(2)
print('--'*36)

for j, t in jogadores.items():
    print(f'''O {j} tirou {t}''')
    sleep(1)

print(' ------ Ranking ------ ')
sleep(1.2)

ranking = sorted(jogadores.items(), key=lambda x: x[1], reverse=True)

for x ,(jogador, valor) in enumerate(ranking, start=1):
    print(f'Em {x}º Lugar {jogador} com {valor} pontos.')
    print('--'*36)
    sleep(1.5)

print('=-'*36)

