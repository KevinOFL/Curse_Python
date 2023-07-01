#Desafio PA v3.0 while

print('=-'*36)
print(' '*22,'\033[7mProgressão Aritimética (PA) v2.0\033[m')
print('=-'*36)

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
primeiro = termo
print('=-'*36)

cont = 1
total = 0
mais = 10

print('Os 10 primeiros termos dessa progressão: ')
while mais != 0:
    total += mais

    while cont <= total:
        print('\033[34;1m{}\033[m -> '.format(termo), end='')
        termo += razao
        cont += 1

    print('PAUSA')

    mais = int(input('''Quantos termos a mais você quer ver: '''))

print('\n','=-'*36)

print('Progressão realizada com o total de {} termos'.format(total))

print('\n','=-'*36)