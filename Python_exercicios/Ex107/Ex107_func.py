# Modulo de funções do exercicio 107

def apresentação():
    """-> Função tipo print de aresentação de titulo do programa"""
    print('=-' * 80)
    print(' ' * 61, '- Trabalhando com modulos -')
    print('=-' * 80)


def linha():
    """-> Função tipo print de linha para customização do programa."""
    print('--' * 80)

def aumentar(num):
    """Aumenta 25% do valor original.
    :param num: Valor original que será somado.
    """
    return num + (num * 0.25)

def diminuir(num):
    """Diminui 35% do valor original.
    :param num: Valor original que será subtraido.
    """
    return  num - (num * 0.35)

def dobro(num):
    """Dobra o valor original.
    :param num: Valor original que será dobrado.
    """
    return  num * 2

def metade(num):
    """Divide o valor original.
    :param num: Valor original que será dividido.
    """
    return num / 2