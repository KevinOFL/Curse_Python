#Desafio vários números

print('=-'*36)
print(' '*22,'\033[7m Vários Números\033[m')
print('=-'*36)

n = 0
contNum = 0
soma = 0

while n != 999:
    n = int(input('''Digite um número: 
    Para parar digite 999
    '''))

    contNum += 1
    soma += n

print('''Você parou o Loop
Quantidade de núemros digitados \033[34;1m{}\033[m
A soma total desses números foi \033[34;1m{}\033[m'''.format(contNum - 1, soma - 999))