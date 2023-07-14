#Desafio Qual é o maior ?

# Funções
def apresentação():
    print('=-'*80)
    print(' '*61, '- Qual é o maior ? -')
    print('=-'*80)
def linha():
    print('--'*80)
def maior(lst):
    m = lst[0]
    for percorrer in lst:
        if percorrer > m:
            m = percorrer
    return m

# Programa principal

lista = list()

apresentação()

while True:
    op = input('''Digite um número \033[33minteiro\033[m pra adicionar a lista,
ou digite "\033[31msair\033[m" para finalizar: ''')

    if op.lower() == 'sair':
        break

    lista.append(int(op))
    linha()

linha()

print(f'''          - RESULTADO -
O maior número adicionado foi \033[34m{maior(lista)}\033[m.''')

linha()