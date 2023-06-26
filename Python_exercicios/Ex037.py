#Desafio base de conversão

print('=-'*60)
print('\033[7mPrograma de base de conversão\033[m')
print('=-'*60)

num = int(input('Digite um número inteiro: '))
base = int(input('''Escolha para qual base deseja converte esse número: 
1 - Binário
2 - Octal
3 - Hexadecimal
Digite o número referente a conversão: '''))

print('=-'*60)

if base == 1:
    print('A representação de {} em bínario é {}{}{}'.format(num,'\033[34m', bin(num), '\033[m'))
elif base == 2:
    print('A representação de {} em octal é {}{}{}'.format(num, '\033[34m', oct(num), '\033[m'))
elif base == 3:
    print('A representação de {} em hexadecimal é {}{}{}'.format(num, '\033[34m', hex(num), '\033[m'))
else:
    print('\033[31mNúmero de opção {} INVÁLIDO!!\033[m'.format(base))

print('=-' * 60)

