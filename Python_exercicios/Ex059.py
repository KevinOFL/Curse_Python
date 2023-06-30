#Desafio menu de operações.

print('=-'*36)
print(' '*26,'\033[7;1m Mneu de operações \033[m')
print('=-'*36)

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

opc = 0

print('=-'*36)

while opc != 5:
    opc = int(input('''---------- Menu ----------
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] novos números
    [5] sair do programa
    Digite operação desejada: '''))

    if opc == 1:
        print('A soma de {} + {} = {}.'.format(n1, n2, n1 + n2))
    elif opc == 2:
        print('A multiplicação de {} * {} = {}.'.format(n1, n2, n1 * n2))
    elif opc == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
        elif n1 < n2:
            print('{} é maior que {}'.format(n2, n1))
        else:
            print('{} e {} são valores iguais'.format(n1, n2))
    if opc == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    if opc == 5:
        break
    else:
        print('Opção inválida!!')

print('Tenha um otimo dia!')

print('=-'*36)