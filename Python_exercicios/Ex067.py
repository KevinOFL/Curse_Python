#Desafio Tabuada 3.0

print('=-'*36)
print(' '*27,'\033[7m Tabuada 3.0 \033[m')
print('=-'*36)

num = int(input('Digite o número que deseja saber a tabuada: '))
cont = 1

print('=-'*36)

while num > 0:
    while cont < 11:
        print(f'{num} x {cont} = \033[34;1m{num*cont}\033[m')
        cont += 1

    print('=-'*36)
    num = int(input('Qual número deseja ver agora ?'))
    cont = 1
    print('=-'*36)

print('\033[32;1mAté a próxima!\033[m')