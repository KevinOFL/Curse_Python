from time import sleep
def cadastrar():
    """Função cadastro do sistema.
    Aqui está toda a trativa de erros antes da inserção dos dados no arquivo,
    para que não ocorra de entrar dados inválidos ou que não seja de possivel leitura..
    """
    while True:
        try:
            nome = input('Digite o nome: ')
            nome.strip().isalpha() #Verifica se é ums string com somente letras.
            break
        except Exception as erro:
            print(f'O erro encontrado foi {erro.__class__}')
    while True:
        try:
            idade = int(input('Digite a idade: '))
            break
        except (TypeError, ValueError):
            print('Valor inválido! Tente novamente.')
        except Exception as erro:
            print(f'O erro encontrado foi {erro.__class__}')

    with open ('pessoas.txt', 'a') as arquivo:
        arquivo.write(f'{nome}     \t{idade}\n') # Aqui irá adicionar os dados que o usuário inseriu.

    print('Dados cadastrado com sucesso!')

def verCadastros():
    """Função ultilziada para percorrer o arquivo e mostrar o nome e idade de cada pessoa cadastrada.
    """
    with open('pessoas.txt', 'r') as arquivo: # Aqui abrimos o arquivo.
        for linha in arquivo:
            dados = linha.strip().split(' \t')  # Verifica se a lista dados possui exatamente 2 elementos.
            if len(dados) == 2:                 # Isso é feito para garantir que a linha contenha nome e idade separados por um espaço e uma tabulação.
                nome, idade = dados
                tam = len(nome)
                print(f'Nome: {nome}{" "*(40-tam)}Idade: {idade}') # Ultilização da variavel tam para alinhar perfeitamente idade.
                sleep(1)
            else:
                print('Formato inválido no arquivo de dados.')

def titulos(num = 3):
    """Função de customização do sistema.
    Serve para diminuir o trablaho, economizar código e melhorar a aparencia do sistema..
    """

    if num == 0:
        print('=-'*30)
        print('  '*8, '-- CADASTRO DE USUÁRIO --')
        print('=-'*30)
    elif num == 1:
        print('=-' * 30)
        print('  ' * 9, '-- MENU PRINCIPAL --')
        print('=-' * 30)
    elif num == 2:
        print('=-' * 30)
        print('  ' * 8, '-- LISTA DE CADASTRADOS --')
        print('=-' * 30)
    elif num == 3:
        print('--' * 30)

def menu():
    """Função menu é onde o sistema começa.
    Serve para trazer uma opção legivel de alguma função do sistema.
    """
    while True:
        try:
            op = int(input('''1 - Cadastrar
2 - Ver cadastros
3 - Sair
ESCOLHA UMA OPÇÂO: '''))
            if op < 1 or op > 3:
                print('Opção inválida!')
                continue
        except (ValueError, TypeError):
            print('Valor inválido! Escolha uma opção valida.')
            continue
        except Exception as erro:
            print(f'ERRO ENCONTRADO -> {erro}')
        else:
            return op


def sistema():
    """Função sistema e onde está agrupado todas as funções,
    em uma ordem básica, primeiro recebemos uma opção válida de alguma função do programa,
    logo em seguida o sistema verifica a opção e transfere o usuário pra alguma das funções.
    """
    while True:
        titulos(1)

        op = menu()

        if op == 1:
            titulos(0)
            cadastrar()

        elif op == 2:
            titulos(2)
            verCadastros()

        elif op == 3:
            print('FINALIZANDO SISTEMA... Até a proxima!')
            break