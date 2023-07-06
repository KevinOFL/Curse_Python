#Desafio 3 lista.

print('=-'*36)
print(' '*27,'\033[7;1m - 3 Lista  - \033[m')
print('=-'*36)

num = 0
valores = list()
par = list()
impar = list()

while True:
    num = input('Digite um número inteiro (Para finalizar digite \033[31;1m"sair"\033[m): ')

    if num.lower() == 'sair':
        break

    if num.isdigit():
        valores.append(int(num))
    else:
        print('Por favor digite um valor numérico!')

for cont in range(len(valores)):
    if valores[cont] % 2 == 0:
        par.append(valores[cont])
    else:
        impar.append(valores[cont])

print('=-'*36)

print(f'''            \033[32;1m Listas \033[m           
lista completa -> \033[32;1m{valores}\033[m
Lista com os valores par -> \033[34m{par}\033[m
Lista com valores impar -> \033[36m{impar}\033[m''')

print('=-'*36)