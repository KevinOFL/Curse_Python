#Desafio maior e menor peso

print('=-'*36)
print(' '*24,'\033[7mMaior e menor peso\033[m')
print('=-'*36)

maior = 0
menor = 0

print('=-'*36)

for c in range(0, 5):
    peso = float(input('Digite seu peso: '))

    if peso > maior:
        maior = peso
    if peso < menor or menor == 0:
        menor = peso

print('=-'*36)

print('''O maior peso é \033[31;1m{}Kg\033[m
O menor peso é \033[34;1m{}Kg\033[m'''.format(maior, menor))