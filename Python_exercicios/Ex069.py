#Desafio estatística de vários tipos de pessoas.

print('=-'*36)
print(' '*27,'\033[7;1m Estatistica de várias pessoas \033[m')
print('=-'*36)

op = 'S'
sexo = ''
idade = 0
contI = contM = contF = 0
media = 0

while True:
    while op == 'S':
        idade = int(input('Digite sua idade: '))
        sexo = input('Qual o seu sexo ? [F/M]').strip().upper()

        while sexo != 'F' and sexo != 'M':
            sexo = input('''Ops, parece que você digitou um sexo inválido.
Por favor digite uma das opções. [F/M]: ''').strip().upper()
            if sexo == 'F' and sexo == 'M':
                break

        if idade > 18: contI += 1
        if sexo == 'M': contM += 1
        if idade < 20 and sexo == 'F': contF += 1

        print('=-'*36)
        break

    op = input('Deseja adicionar mais alguma pessoa ? [S/N]').strip().upper()
    if op == 'N':
        break

print(f'''     \033[34;1mEstatisticas\033[m     
\033[34m{contM+contF}\033[m pessoas foram cadastradas.
\033[34m{contI}\033[m tem mais de 18 anos.
\033[34m{contM}\033[m homens foram cadastrados.
\033[34m{contF}\033[m mulheres tem menos de 20 anos de idade.''')