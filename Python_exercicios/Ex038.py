#Desafio dois números

print('=-'*60)
print('\033[7mPrograma de comparação\033[m')
print('=-'*60)

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

print('=-'*60)

if n1 > n2:
    print('O {}primeiro valor{} {} é MAIOR'.format('\033[33m', '\033[m', n1))

elif n2 > n1:
    print('O {}segundo valor{} {} é MAIOR'.format('\033[33m', '\033[m', n2))

else:
    print('O {}não existe{} valor maior os número {} e {} são iguais'.format('\033[31m', '\033[m', n1, n2))

print('=-'*60)