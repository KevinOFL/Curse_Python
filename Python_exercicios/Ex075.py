#Desafio 4 números

print('=-'*36)
print(' '*26,'\033[7;1m - 4 números  - \033[m')
print('=-'*36)

v1 = int(input('Digite 1º número: '))
v2 = int(input('Digite 2º número: '))
v3 = int(input('Digite 3º número: '))
v4 = int(input('Digite 4º número: '))

t = (v1, v2, v3, v4)
n1 = n2 = n3 = 0

for c in range(0, len(t)):
    if t[c] == 9: n1 += 1

    if t[c] == 3: n2 = t.index(3)

    if t[c] % 2 == 0:
        print(f'Número par {t[c]}')

print(f'O número 9 apareceu {n1} vezes')
print(f'O valor 3 foi inserido na posição {n2}º')

print('=-'*36)