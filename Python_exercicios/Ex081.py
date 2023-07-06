#Desafio Relátorio de número.

print('=-'*36)
print(' '*22,'\033[7;1m - Relátorio de número  - \033[m')
print('=-'*36)

num = 0
valores = list()

while True:
    num = input('Digite um número inteiro (Para finalizar digite \033[31;1m"sair"\033[m): ')
    if num.lower() == 'sair':
        break
    valores.append(int(num))

valores.sort(reverse=True)

print('=-'*36)

print(f'''           Relátorio           
Foram digitado \033[34;1m{len(valores)}\033[m valores.
Lista decrecente: \033[35;1m{valores}\033[m.''')

if 5 in valores:
    valor = valores.index(5)
    print(f'O valor 5 \033[34mestá presente\033[m na lista no indice {valor}.')
else:
    print(f'\033[31mO valor 5 não está presente na lista.\033[m')

print('=-'*36)