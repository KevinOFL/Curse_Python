# Modulo de funções do exercicio 109
# Reutilizando arquivos do exercicio 109 para não mudar o código de lá.

def apresentação():
    """-> Função tipo print de aresentação de titulo do programa"""
    print('=-' * 80)
    print(' ' * 61, '- Trabalhando com modulos -')
    print('=-' * 80)


def linha():
    """-> Função tipo print de linha para customização do programa."""
    print('--' * 80)

def aumentar(num = 0, taxa = 0, formato = False):
    """Aumenta o valor original.
    :param num: Valor original que será somado.
    :param taxa: Porcentagem da taxa a ser somada ao valor original.
    :param formato: Se esse parametro tiver como false o resultado não vai ser formatado pela função moeda()
    Se estiver como True ele vai ser formatado.
    """
    res = num + (num * taxa/100)
    return res if formato is False else moeda(res)

def diminuir(num = 0, taxa = 0, formato = False):
    """Diminui o valor original.
    :param num: Valor original que será subtraido.
    :param taxa: Porcentagem da taxa a ser subtraida ao valor original.
    :param formato: Se esse parametro tiver como false o resultado não vai ser formatado pela função moeda()
    Se estiver como True ele vai ser formatado
    """
    res = num - (num * taxa/100)
    return  res if formato is False else moeda(res)

def dobro(num = 0, formato = False):
    """Dobra o valor original.
    :param num: Valor original que será dobrado.
    :param formato: Se esse parametro tiver como false o resultado não vai ser formatado pela função moeda()
    Se estiver como True ele vai ser formatado
    """
    res =  num * 2
    return res if formato is False else moeda(res)

def metade(num = 0, formato = False):
    """Divide o valor original.
    :param num: Valor original que será dividido.
    :param formato: Se esse parametro tiver como false o resultado não vai ser formatado pela função moeda()
    Se estiver como True ele vai ser formatado
    """
    res = num / 2
    return res if formato is False else moeda(res)

def moeda(num = 0, moeda = 'R$'):
    """Função de formatação para valores monetarios.
    """
    return f'{moeda}{num:.2f}'.replace('.', ',')

def resumo(num = 0, taxa = 0):
    """Função resumo e praticamente um print inteiro sobre o programa."""
    linha()
    print(f'''              - - RESULTADO DO VALOR RS{moeda(num)} - -''')
    linha()
    print(f'''Aumentamos {taxa}% do valor original {moeda(num)} \t-> {aumentar(num, taxa, True)}
Diminuimos {taxa}% do valor original {moeda(num)} \t-> {diminuir(num, taxa, True)}
Dobramos o valor original {moeda(num)}     \t\t-> {dobro(num, True)}
Dividimos o valor orinal {moeda(num)}     \t\t-> {metade(num, True)}''')
    linha()