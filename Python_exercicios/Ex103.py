#Desafio Ficha do jogador

# Packages imports
from time import sleep

# Funções
def apresentação():
    """-> Função tipo print de aresentação de titulo do programa"""
    print('=-'*80)
    print(' '*61, '- Ficha do jogador -')
    print('=-'*80)
def linha():
    """-> Função tipo print de linhas para customização do programa."""
    print('--'*80)
def ficha(n, g):
    """-> Função de exibição de ficha de jogador com 2 parâmetros.
    :param n: nome do jogador inserido pelo usuário.
    :param g: total de gols inserido pleo usuário.
    Caso nenhum parâmetro seja inserido ou somente um a função irá verificar
    e irá trazer um ficha baseada nos dados inseridos.
    """

    if not n and not g:
        print('     - Ficha do jogador desconhecido -')
        print('O jogador <desconhecido> marcou 0 gols nessa temporada.')
    elif not n:
        print(f'     - Ficha do jogador desconhecido -')
        print(f'O jogador <desconhecido> marcou {g} gols nessa temporada.')
    elif not g:
        print(f'     - Ficha do jogador {n} -')
        print(f'O jogador {n} não marcou gols nessa temporada.')
    else:
        print(f'     - Ficha do jogador {n} -')
        print(f'O jogador {n} marcou {g} gols nessa temporada.')

# Programa principal

apresentação()
sleep(0.5)

nome = input('Digite o nome do jogador: ')
gols = input('Quantos gols o jogador marcou: ')
sleep(1.5)

linha()

ficha(nome, gols)

linha()

