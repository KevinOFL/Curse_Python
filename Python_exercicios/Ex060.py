#Desafio fatorial while 2.0

print('=-'*36)
print(' '*29,'\033[7;1m Fatorial v2.0 \033[m')
print('=-'*36)

usu = int(input('Digite um número inteiro: '))

c = usu
f = 1

while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))