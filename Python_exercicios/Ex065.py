#Desafio Média de números

print('=-'*36)
print(' '*22,'\033[7m Média de Números \033[m')
print('=-'*36)

cont1 = 1
num = 0
op = 'S'
soma = 0
maior = 0
menor = 0

while op in 'Ss':
    num = int(input('''Digite o {}º Número'''.format(cont1)))
    soma += num

    if cont1 == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    op = input('Deseja digitar mais algum número ? [SIM/NAO').upper().strip()[0]
    cont1 += 1

print('=-'*36)

print('''A média etre todos os valores foi {:.2f}
O maior valor é {}
E o menor valor foi {}'''.format((soma / cont1), maior, menor))

print('=-'*36)