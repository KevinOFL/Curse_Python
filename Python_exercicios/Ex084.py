#Dedafio lista de pessoas

from math import floor

print('=-'*36)
print(' '*24,'\033[7;1m - Lista de pessoas  - \033[m')
print('=-'*36)

lista = list()
aux = list()
baixo = list()
alto = list()
cont = soma = 0


while True:
    print('Para finalizar o programa digite "\033[34;1mSair\033[m".')
    nome = input('''Digite seu nome: ''')

    if nome.lower() == 'sair':
        break

    peso = float(input('Digite seu peso: '))

    if nome.isalpha():
        aux.append(nome)
        aux.append(peso)
        soma += peso
        lista.append(aux[:])
        aux.clear()
        cont += 1
    else:
        print('\033[31m=-\033[m'*36)
        print(f'Valor \033[31m{nome}\033[m inválido! Por favor digite um valor valido.')
        print('\033[31m=-\033[m' * 36)

for p in lista:
    media = soma /cont
    if p[1] >= media:
        alto.append(p[0])
    else:
        baixo.append(p[0])

print('=-'*36)

print(f'''          \033[7m Relatório \033[m           
O total de pessoas cadastradas foi \033[34m{cont}\033[m.
Pessoas com maior peso perante a média ({floor(media)}): \033[31m{alto}\033[m.
Pessoas com menor peso perante a média ({floor(media)}): \033[34m{baixo}\033[m''')

print('=-'*36)