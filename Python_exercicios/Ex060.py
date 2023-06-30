#Desafio fatorial while 2.0

print('=-'*36)
print(' '*29,'\033[7;1m Fatorial v2.0 \033[m')
print('=-'*36)

soma = 0
cont = 0

usu = int(input('Digite um número inteiro: '))
usu1 = usu

f = usu-1

while f != 0:
    soma = usu * f
    print('{} * {} = {}'.format(usu,f,soma))
    usu = soma
    f -= 1
    cont += soma

print('O fatorial de {} é {}'.format(usu1, cont))