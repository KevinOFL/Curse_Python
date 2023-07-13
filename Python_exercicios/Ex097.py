# Desafio String acompanhada de linhas

# Funções
def apresentação():
    print('=-'*80)
    print(' '*61, '- String acompanhada de cobras -')
    print('=-'*80)
def linha():
    print('--'*80)

def acopanha(stgr):
    for c in range(len(stgr)+1):
        print('~',end='')
    print('\n',stgr)
    for c in range(len(stgr)+1):
        print('~',end='')

# Programa principal

apresentação()

frase = input('Digite alguma coisa: ')

acopanha(frase)

linha()