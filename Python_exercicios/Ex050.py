#Desafio seis núemros pares

print('=-'*36)
print(' '*22,'\033[7mSoma de seis números pares\033[m')
print('=-'*36)

soma = 0

for c in range(0, 6):
    num = int(input('Digite um número inteiro: '))

    if num % 2 != 1:
        aux = num
        soma = soma + aux

print('A soma total foi {}{}{}'.format('\033[32;1m', soma, '\033[m'))

