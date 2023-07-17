#Desafio Ficha do jogador

# Packages imports


# Funções
def apresentação():
    """-> Função tipo print de aresentação de titulo do programa"""
    print('=-'*80)
    print(' '*61, '- leia int: -')
    print('=-'*80)
def linha():
    """-> Função tipo print de linhas para customização do programa."""
    print('--'*80)
def leiaInt(i):
    """-> Função tipo input onde só aceita números inteiros.
    :param i: Uma string que recebe o pedido do usário.
    Logo após o programa receber o valor ele retorna para a variavel pergunta,
    caso o valor não seja um número inteiro o programa continuara a solicitar o valor.
    """
    pergunta = input(f'{i}')

    if pergunta.isnumeric():
        return  pergunta
    else:
        while True:
            print('\033[31mValor inválido!\033[m')
            pergunta = input(f'{i}')
            if pergunta.isnumeric():
                break
        return  pergunta

# Programa principal

apresentação()

x = leiaInt('Digite um número: ')
print(f'Você digitou o número \033[32m{x}\033[m. ')

linha()