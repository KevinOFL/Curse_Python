#Desafio PA v2.0 while

print('=-'*36)
print(' '*22,'\033[7mProgressão Aritimética (PA) v2.0\033[m')
print('=-'*36)

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

print('=-'*36)

cont = 0
soma = termo + razao

print('Os 10 primeiros termos dessa progressão: ')
print('\033[34;1m{}\033[m'.format(termo))
while cont != 9:
    print('\033[34;1m{}\033[m'.format(soma))
    termo = soma
    soma = termo + razao
    cont += 1

print('=-'*36)