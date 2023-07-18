def leiaDinheiro(msg):
    """Função leiaDinheiro é uma validadora da entrada de valor do usuário.
    :param msg: É um String ou seja a pergunta do pragrama para entrar algum valor.
    Caso o usuário digite um valor com virgula será tratado para que não de erro.
    E caso ele digite somente letras e espações juntos será tratado para que ele redigite o valor novamente.
    """
    valido = False
    while not valido:
        entrada = input(msg).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'ERRO: \033[31m{entrada}\033[m é um valor inválido!')
        else:
            valido = True
            return float(entrada)