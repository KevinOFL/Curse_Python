#Desafio Matriz

print('=-'*36)
print(' '*28,'\033[7;1m - Matriz  - \033[m')
print('=-'*36)

matriz = []

for p in range(0, 3):
    aux = []
    for s in range(0, 3):
        num = int(input(f'Digite um valor para [{p},{s}]: '))
        aux.append(num)
    matriz.append(aux[:])

print('=-'*36)

print('''\033[7m     MATRIZ   \033[m''')
for c in matriz:
    for x in matriz:
        print(f'''[ {x[1]} ]''', end='')
    print()

print('=-'*36)