def apresentação():
    """-> Função tipo print de aresentação de titulo do programa"""
    print('=-'*80)
    print(' '*61, '- leia int e float -')
    print('=-'*80)
def linha():
    """-> Função tipo print de linhas para customização do programa."""
    print('--'*80)
def leiaInt(i):
    """-> Função tipo input onde só aceita números inteiros.
    :param i: Uma string que recebe o pedido do usário.
    Logo após o programa receber o valor ele retorna para a variavel pergunta,
    caso o valor não seja um número inteiro o programa irá iniciar a trativa de erro até o usário digitar um valor inteiro.
    """
    while True:
        try:
            perguntaInt = int(input(f'{i}'))
        except (ValueError, TypeError):
            print(f'Você digitou um valor inválido! Tente novamente.')
            continue
        except Exception as erro:
            print(f'O erro foi {erro.__class__}')
            continue
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar esse valor: ')
            return  0
        else:
            return perguntaInt

def leiaFloat(i):
    """Função leiaFloat é uma validadora da entrada tipo float.
    :param i: É um String ou seja a pergunta do pragrama para entrar algum valor.
    Caso o usuário digite um valor com virgula será tratado para que o programa entenda que é um ponto.
    E caso ele digite somente letras e espações juntos será tratado para que ele redigite o valor novamente.
    """
    while True:
        try:
            perguntaFloat = float(input(f'{i}').strip())
        except (ValueError, TypeError):
            print(f'Você digitou um valor inválido! Tente novamente.')
            continue
        except Exception as erro:
            print(f'O erro foi {erro.__class__}')
            continue
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar esse valor: ')
            return  0
        else:
            return perguntaFloat
