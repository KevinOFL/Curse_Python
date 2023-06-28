#Desafio Tabuada 2.0

print('=-'*36)
print(' '*27,'\033[7mTabuada 2.0\033[m')
print('=-'*36)

num = int(input('Digite o número que deseja saber a tabuada: '))
fim = int(input('Até que número você quer que vá: '))

print('=-'*36)

for c in range(0, fim+1):
    print('{} x {} = {}'.format(num, c, num*c))

print('\033[32;1mFIM\033[m')