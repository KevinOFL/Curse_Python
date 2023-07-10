print('=-'*36)
print(' '*28, '\033[7;1m - Matriz v2.0  - \033[m')
print('=-'*36)

matriz = []
cont = 0
soma = 0
auxx = 0

for p in range(0, 3):
    aux = []
    for s in range(0, 3):
        num = int(input(f'Digite um valor para [{p},{s}]: '))
        aux.append(num)

        if num % 2 == 0:
            cont += num

        if s == 2:
            soma += num

        if s == 1:
            if auxx == 0:
                auxx = num
            elif auxx < num:
                auxx = num

    matriz.append(aux[:])

print('=-'*36)

print('''\033[7m     MATRIZ   \033[m''')
for linha in matriz:
    for valor in linha:
        print(f'[ {valor} ]', end=' ')
    print()

print(f'''\033[7m     Resultados \033[m
A soma de todos os valores pares digitados foi \033[34;1m{cont}\033[m.
A soma da terceira coluna \033[35;1m{soma}\033[m.
E o maior valor da segunda coluna foi \033[36;1m{auxx}\033[m''')

print('=-'*36)