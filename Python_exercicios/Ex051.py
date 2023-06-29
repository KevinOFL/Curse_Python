#Desafio PA

print('=-'*36)
print(' '*22,'\033[7mProgressão Aritimética (PA)\033[m')
print('=-'*36)

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

print('=-'*36)

print('Os 10 primeiros termos dessa progressão: ')
for c in range(termo, razao*10+1, razao):
    print('\033[34;1m{}\033[m'.format(c))

print('=-'*36)
