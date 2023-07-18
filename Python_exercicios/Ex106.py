#Desafio Sistema help

# Packages imports
from time import sleep
from math import floor

# Funções
def apresentação():
    """-> Função tipo print de aresentação de titulo do programa"""
    print('=-'*80)
    print(' '*61, '- Sistema help -')
    print('=-'*80)

def linha():
    """-> Função tipo print de linhas para customização do programa."""
    print('--'*80)

def sistemaHelp():
    while True:
        """
        Função sistemaHelp serve para automatizar e economizar tempo
        para ler documentações do python e suas bibliotecas.
        """
        arg = input('''Para sair do programa digite \033[31m"sair"\033[m.
Qual função ou biblioteca deseja ver: ''')
        if arg.lower() == 'sair':
            print('\033[35mTomara que eu tenha te ajduado. Até logo!\033[m')
            break
        else:
            
            print(help(arg))
        linha()


# Programa principal

apresentação()

sistemaHelp()