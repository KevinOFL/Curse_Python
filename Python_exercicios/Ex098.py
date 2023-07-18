# Desafio Tipos de contagens

from time import sleep

# Funções
def apresentação():
    print('=-'*80)
    print(' '*61, '- Tipos de contagenss -')
    print('=-'*80)
def linha():
    print('--'*80)

def contagem():
    print('Contagem de 1 até 10 de 1 em 1.')
    for x in range(1, 11):
        print(x, end=" ")
        sleep(0.5)
    print('FIM...')
    linha()

    print('Contagem de 10 até 0 de 2 em 2.')
    for y in range(10, -1, -2):
        print(y, end=' ')
        sleep(0.5)
    print('FIM...')

    linha()

    print('Agora é sua vez de criar um contagem: ')

    linha()

    inicio = int(input('Inicio: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))

    linha()

    if inicio < fim:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
        for contador in range(inicio, fim + 1, passo):
            print(contador, end=' ')
            sleep(0.5)
        print('FIM...')
    elif inicio > fim and passo > 0:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
        for contador in range(inicio, fim + 1, -passo):
            print(contador, end=' ')
            sleep(0.5)
        print('FIM...')
    elif inicio > fim and passo < 0:
        print(f'Contagem de {inicio} até {fim} de {-passo} em {-passo}.')
        for contador in range(inicio, fim - 1, passo):
            print(contador, end=' ')
            sleep(0.5)
        print('FIM...')
    elif inicio > fim and passo == 0:
        print(f'Contagem de {inicio} até {fim} de {1} em {1}.')
        for contador in range(inicio, fim - 1, -1):
            print(contador, end=' ')
            sleep(0.5)
        print('FIM...')
    elif inicio < fim and passo == 0:
        print(f'Contagem de {inicio} até {fim} de {1} em {1}.')
        for contador in range(inicio, fim + 1 , 1):
            print(contador, end=' ')
            sleep(0.5)
        print('FIM...')


# Programa principal

apresentação()

contagem()

linha()