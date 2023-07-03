#Desafio estatística de vários tipos de pessoas.

print('=-'*36)
print(' '*27,'\033[7;1m Estatistica de venda de produtos \033[m')
print('=-'*36)

aux = contM = preco = soma = 0
auxNome = nomePro = ''
op = 'S'

while True:
    while op == 'S':
        nomePro = input('Digite o nome do produto: ')
        preco = float(input('Digite o preço do produto: R$'))

        while preco <= 0:
            preco = float(input('''Ops, você digitou um valor menor que zero.
Digite outro por favor R$'''))
            if preco < 0:
                break

        soma += preco

        if preco > 1000: contM += 1

        if aux == 0:
            aux = preco
            auxNome = nomePro
        if preco < aux:
            aux = preco
            auxNome = nomePro
        break
    print('=-' * 36)

    op = input('Deseja adicionar mais algun produto ? [S/N]').strip().upper()
    if op == 'N':
        break

print('=-'*36)

print(f'''     \033[32;1mEstatisticas de vendas\033[m     
O total gasto na compra foi R$\033[32;1m{soma}\033[m.
Foram \033[32;1m{contM}\033[m produtos com valor maior que R$1000,00.
O produto mais barato foi \033[33;1m{auxNome}\033[m no preço de R$\033[32;1m{aux}\033[m''')