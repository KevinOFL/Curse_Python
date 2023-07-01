#Desafio sequência de Fibonacci

print('=-'*36)
print(' '*22,'\033[7mSequência de Fibonacci\033[m')
print('=-'*36)

n1 = int(input('Digite um número inteiro: '))

t1 = 0
t2 = 1
cont = 0

print('=-'*36)
print('{} -> {} '.format(t1, t2), end='')

while cont <= n1:
    t3 = t1 + t2
    print('-> {} '.format(t3),end='')
    t1 = t2
    t2 = t3
    cont += 1

print('\n','FIM')
print('=-'*36)