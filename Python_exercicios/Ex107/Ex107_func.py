# Modulo de funções do exercicio 107

def apresentação():
    """-> Função tipo print de aresentação de titulo do programa"""
    print('=-' * 80)
    print(' ' * 61, '- Trabalhando com modulos -')
    print('=-' * 80)


def linha():
    """-> Função tipo print de linha para customização do programa."""
    print('--' * 80)

def aumentar(num, taxa):
    """Aumenta 25% do valor original.
    :param num: Valor original que será somado.
    """
    res = num + (num * taxa/100)
    return res

def diminuir(num, taxa):
    """Diminui o valor original.
    :param num: Valor original que será subtraido.
    """
    res = num - (num * taxa/100)
    return  res

def dobro(num):
    """Dobra o valor original.
    :param num: Valor original que será dobrado.
    """
    res =  num * 2
    return res

def metade(num):
    """Divide o valor original.
    :param num: Valor original que será dividido.
    """
    res = num / 2
    return res