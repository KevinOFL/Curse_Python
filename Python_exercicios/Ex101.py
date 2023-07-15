#Desafio Avaliação de voto

# Packages imports
from datetime import date
from time import sleep

# Funções
def apresentação():
    """-> Função tipo print de aresentação de titulo do programa"""
    print('=-'*80)
    print(' '*61, '- Avaliação de voto -')
    print('=-'*80)
def linha():
    """-> Função tipo print de linhas para customização do programa."""
    print('--'*80)
def avaliaVoto():
    """-> Função de verificação de voto sem parâmetros.
    Ultiliza das variaveis:
    ano, idade, ensino e titulo para efetuar a veficação com if e elif.
    """

    ensino = input('Você é analfabeto ? [S/N]: ')
    titulo = input('Você possui titulo de eleitor? [S/N]:')
    sleep(0.5)

    linha()
    sleep(2)
    print('      - ANALISANDO DADOS... -')
    linha()
    sleep(2)

    if idade == 16 or idade == 17 or idade > 70:
        print(f'''      -- RESULTADO --
Você possui \033[34m{idade}\033[m nesse caso seu voto é do tipo facultativo - Voto opcional.''')
    elif ensino.lower() == 's':
        print(f'''      -- RESULTADO --
Você possui \033[34m{idade}\033[m e é uma pessoa analfabeta, nesse caso seu voto é do tipo facultativo - Voto opcional.''')
    elif idade > 18 and idade < 70 and ensino.lower() == 'n' and titulo.lower() == 's':
        print(f'''      -- RESULTADO --
Você possui \033[34m{idade}\033[m nesse caso seu voto é do tipo obrigatório - Obrigado a votar.''')
    elif titulo.lower() == 'n':
        print('\033[31mÉ preciso tirar titulo de eleitor para exercer o direito de votar.\033[m')

# Programa principal
atual = date.today().year

apresentação()

ano = int(input('Digite seu ano de nascimento: '))
idade = atual - ano

# Verifica se digitou uma idade valida acima de 0 anos.
if idade < 0:
    while True:
        ano = int(input(f'''Idade {idade} inválida.
   Por favor digite seu ano de nascimento correto: '''))
        idade = atual - ano
        if idade > 0:
            break

linha()

avaliaVoto()

linha()