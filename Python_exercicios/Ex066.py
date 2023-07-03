#Desafio vários números v2.0

print('=-'*36)
print(' '*25, '\033[7;1mVários núemros v2.0\033[m')
print('=-'*36)

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n

print('=-'*36)

print(f'A soma vale \033[32;1m{s}\033[m')

print('=-'*36)