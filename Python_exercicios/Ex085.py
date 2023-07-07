#Desafio Lista de pares e impar

print('=-'*36)
print(' '*21,'\033[7;1m - Lista de pares e impar  - \033[m')
print('=-'*36)

par = list()
impar = list()
lista = list()

for c in range(0, 7):
    num = int(input(f'Digite o {c+1}º número: '))

    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

lista.append(par[:])
lista.append(impar[:])
lista[0].sort()
lista[1].sort()

print('=-'*36)

print(f'''          \033[7m Lista \033[m          
Lista de valores pares em ordem crecente: \033[32m{lista[0]}\033[m
Lista de valores impar em ordem crecente: \033[34m{lista[1]}\033[m''')

print('=-'*36)