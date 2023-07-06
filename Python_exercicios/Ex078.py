#Desafio 5 valores numéricos.

print('=-'*36)
print(' '*23,'\033[7;1m - Valores numéricos  - \033[m')
print('=-'*36)

num = list()
maior = menor = indMai = indMen = c = 0

for v in range(0, 5):
    num.append(int(input(f'Digite o {v+1}º valor: ')))

    if maior == 0 and menor == 0:
        maior = num[v]
        menor = num[v]
    elif num[v] > maior:
        maior = num[v]
        indMai = num.index(maior)
    elif num[v] < menor:
        menor = num[v]
        indMen = num.index(menor)

    v += 1

print('=-'*36)

print(f'''O maior valor foi \033[34;1m{maior}\033[m no indice \033[32m{indMai+1}\033[m
O menor valor foi \033[34;1m{menor}\033[m no indice \033[32m{indMen+1}\033[m''')

print('=-'*36)