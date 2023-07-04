#Desafio número por extenso

print('=-'*36)
print(' '*27,'\033[7;1m Números por extenso \033[m')
print('=-'*36)

nums = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezeseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
valor = 0
op = 0

while True:
    op = int(input('Digite um número de \033[34m0 & 20\033[m: '))

    if 0 <= op <= 20:
        valor = nums[op]
        print(f'O valor que você digitou foi \033[34;1m{valor}\033[m.')
        break
    else:
        print('\033[31mVocê digitou um valor fora do limite entre 0 & 20.\033[m')

print('=-'*36)