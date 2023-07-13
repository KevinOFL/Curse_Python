#Desafio aréa com função def

import math

# Funções
def apresentação():
    print('=-'*80)
    print(' '*64, '- Área com função def -')
    print('=-'*80)
def linha():
    print('--'*80)

def area(a, b):
    print('             - RESULTADO -')
    print(f'A área do terreno : \033[33m{altura}x{largura}\033[m é de \033[32m{(a*b)*2:.2f}\033[mm²')


# Programa principal

apresentação()

altura = float(input('Digite a altura: '))
largura = float(input('Digite a largura: '))

linha()

area(altura,largura)

linha()

