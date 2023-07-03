#Desafio jogo par ou impar

from random import randint

print('=-'*36)
print(' '*27,'\033[7m Jogo par ou impar v1.0 \033[m')
print('=-'*36)

pc = randint(0, 100)
n = int(input('Escolha um número: '))
op = input('Par ou Impar ? [P/I]').strip().upper()
soma = n + pc
contV = 0

while n >= 0:
    while True:
        if soma % 2 == 0 and op == 'P':
            print(f'''Você jogou {n} e o computador {pc}.
Soma deles é {soma}.
DEU PAR!''')
            break
        elif soma % 2 == 1 and op == 'I':
            print(f'''Você jogou {n} e o computador {pc}.
Soma deles é {soma}.
DEU IMPAR!''')
            break
        elif soma % 2 == 0 and op == 'I':
            print(f'''Você jogou {n} e o computador {pc}.
Soma deles é {soma}.
DEU IMPAR!''')
            print('=-'*36)
            print('Você Perdeu!')
            print('=-'*36)
            n = False
            break
        elif soma % 2 == 1 and op == 'P':
            print(f'''Você jogou {n} e o computador {pc}.
Soma deles é {soma}.
DEU IMPAR!''')
            n = False
            break

    if n == False and contV >= 0:
        print('=-' * 36)
        print(f'''\033[31;1mVOCÊ PERDEU!\033[m
Ganhou \033[34;1m{contV}\033[m vezes''')
        print('=-' * 36)
        break
    else:
        print('=-'*36)
        print('\033[32;1mVOCÊ VENCEU!\033[m')
        print('Vamos outro round!')
        print('=-' * 36)
        contV += 1
        n = int(input('Escolha um número: '))
        op = input('Par ou Impar ? [P/I]').strip().upper()
