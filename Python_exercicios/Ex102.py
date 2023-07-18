#Desafio Ver ou não fatorial ?

# Packages imports
from time import sleep

# Funções
def apresentação():
    """-> Função tipo print de aresentação de titulo do programa"""
    print('=-'*80)
    print(' '*61, '- Ver ou não fatorial ? -')
    print('=-'*80)
def linha():
    """-> Função tipo print de linhas para customização do programa."""
    print('--'*80)
def fatorial(n, show=True):
    """
    Calcula o fatorial de um número n.
    Parâmetros:
        - n: número inteiro positivo
        - show (opcional): valor booleano para mostrar ou não o processo de cálculo (padrão: True)
    Retorna:
        - O fatorial de n.
    """
    resultado = 1
    if show:
        print(f'Calculando o fatorial de {n}...')
    for i in range(1, n + 1):
        resultado *= i
        if show:
            print(f'Multiplicando por {i}...')
    if show:
        print(f'O fatorial de {n} é {resultado}')
    elif show == False:
        print(f'O fatorial de {n} é {resultado}')
    return resultado

# Programa principal

apresentação()

fatorial(8, show=True)

linha()