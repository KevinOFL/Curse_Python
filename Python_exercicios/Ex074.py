#Desafio 5 números aléatorios

from random import randint

print('=-'*36)
print(' '*22,'\033[7;1m - 5 números aléatorio - \033[m')
print('=-'*36)

alea = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print(f'''          \033[34m- Resultado -\033[m          
Os 5 valorés são: \033[33m{alea}\033[m
O maior valor é: \033[34m{max(alea)}\033[m
O menor valor é: \033[31m{min(alea)}\033[m''')

print('=-'*36)