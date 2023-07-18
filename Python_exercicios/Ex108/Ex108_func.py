# Modulo de funções do exercicio 108
# Ultilizamos um copia e cola do exercicio 107 para não mudar o código de lá.

def apresentação():
    """-> Função tipo print de aresentação de titulo do programa"""
    print('=-' * 80)
    print(' ' * 61, '- Trabalhando com modulos -')
    print('=-' * 80)


def linha():
    """-> Função tipo print de linha para customização do programa."""
    print('--' * 80)

def aumentar(num = 0, taxa = 0):
    """Aumenta o valor original.
    :param num: Valor original que será somado.
    """
    res = num + (num * taxa/100)
    return res

def diminuir(num = 0, taxa = 0):
    """Diminui o valor original.
    :param num: Valor original que será subtraido.
    """
    res = num - (num * taxa/100)
    return  res

def dobro(num = 0):
    """Dobra o valor original.
    :param num: Valor original que será dobrado.
    """
    res =  num * 2
    return res

def metade(num = 0):
    """Divide o valor original.
    :param num: Valor original que será dividido.
    """
    res = num / 2
    return res

def moeda(num = 0, moeda = 'R$'):
    """Função de formatação para valores monetarios.
    """
    return f'{moeda}{num:.2f}'.replace('.', ',')