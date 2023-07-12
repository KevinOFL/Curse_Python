#Desafio dicionario de pessoas

print('=-'*36)
print(' '*18, '\033[7;1m - Dicionario de pessoas  - \033[m')
print('=-'*36)

listaF = list()
lista = list()
disci = dict()
quantP = soma = media =  0

while True:
    opc = input('Deseja adicionar alguma pessoa? "\033[33m[S/N]\033[m" :')
    if opc.lower() == 'n':
        break

    aux = []
    disci['nome'] = input('Digite o nome: ')
    disci['sexo'] = input('Qual o sexo? [M/F]: ')
    if disci['sexo'].lower() != 'f' and disci['sexo'].lower() != 'm' :
        while True:
            print('valor inválido! Por favor digite um válido.')
            disci['sexo'] = input('Qual o sexo? [M/F]: ')
            if disci['sexo'].lower() == 'm' or disci['sexo'].lower() == 'f':
                break
    disci['idade'] = int(input('Qual a idade? '))

    aux.append(disci.copy())

    if disci['sexo'].lower() == 'f':
        listaF.append(aux[:])

    lista.append(aux[:])
    soma += disci['idade']
    quantP += 1
    disci.clear()

media = soma / quantP
print('=-'*36)

print(' ---------- Resumo ---------- ')
print(f'''--Foram no total \033[34m{quantP}\033[m pessoas cadastradas. 
--A média de idade do grupo foi \033[34m{media:.1f}\033[m
--Todas a mulheres que foram cadastras: ''')
for pessoas in listaF:
    print('\033[34m',pessoas[0]['nome'],'\033[m')

print('\n --Pessoas que estão com a idade acima da média: ')
for pessoas in lista:
    if pessoas[0]['idade'] > media:
        print(f'\033[32m{pessoas[0]["nome"]}\033[m, sexo = {pessoas[0]["sexo"]} com {pessoas[0]["idade"]}')

print('=-'*36)