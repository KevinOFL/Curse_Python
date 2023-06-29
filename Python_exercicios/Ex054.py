#Desafio maioridade

from datetime import date

print('=-'*36)
print(' '*28,'\033[7mMaioridade\033[m')
print('=-'*36)

atual = date.today().year
maior = 0
menor = 0

for c in range(0, 7):
    dataUsu = int(input('Digite seu ano de nascimento: '))
    somaIdade = atual - dataUsu
    if somaIdade >= 18:
        maior += 1
    else:
        menor += 1

print('=-'*36)

print('''\033[34;1m{}\033[m Atingiram a maior idade.
\033[32;1m{}\033[m ainda não são de maior.'''.format(maior, menor))

print('=-'*36)