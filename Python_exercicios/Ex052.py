#Desafio número primo

print('=-'*36)
print(' '*28,'\033[7mNúmero primo\033[m')
print('=-'*36)

num = int(input('Digite um número: '))
tot = 0

for c in range(1, num+1):
    if num % c == 0:
        print('\033[32m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')

print('\nO número {} foi divisivel {} vezes'.format(num, tot))

if tot == 2:
    print('Ele é PRIMO!')
else:
    print('Ele não é PRIMO!')
