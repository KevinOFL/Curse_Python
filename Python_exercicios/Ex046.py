#Desafio contagem regressiva.

from time import sleep

print('=-'*36)
print(' '*25,'\033[7mContagem regressiva\033[m')
print('=-'*36)

for c in range(10, -1, -1):
    print(c)
    sleep(1)

print('\033[31;1mBUM!! BUM!! POW!!!!\033[m')