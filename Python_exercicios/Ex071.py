#Desafio Caixa eletrônico

print('=-'*36)
print(' '*27,'\033[7;1m Caixa eletrônico \033[m')
print('=-'*36)

c200 = c100 = c50 = c20 = c10 = c5 = aux = soma = 0

valor = int(input('''Possuimos somente cédulas de 200, 100, 50, 20, 10 e 5.
Digite o valor a ser sacado: R$'''))

if valor < 4.99:
    print('\033[31;1mNão possuimos cédulas para esse valor!\033[m')
else:
    while True:
        
        if valor - 200 >= 0:
            c200 += 1
            valor = valor - 200
        elif valor - 100 >= 0:
            c100 += 1
            valor = valor - 100
        elif valor - 50 >= 0:
            c50 += 1
            valor = valor - 50
        elif valor - 20 >= 0:
            c20 += 1
            valor = valor - 20
        elif valor - 10 >= 0:
            c10 += 1
            valor = valor - 10
        elif valor - 5 >= 0:
            c5 += 1
            valor = valor - 5
        elif valor < 5:
            soma = (c200 * 200) + (c100 * 100) + (c50 * 50) + (c20 * 20) + (c10 * 10) + (c5 * 5)
            aux = valor
            break

        print('=-'*36)


print(f'''          \033[32;1mCédulas a ser sacadas\033[m

R$200.00 = {c200}
R$100.00 = {c100}
R$50.00 = {c50}
R$20.00 = {c20}
R$10.00 = {c10}
R$5.00 = {c5}
\033[31;1mE sobra R${aux} por falta de cédula\033[m.''')

print(f'\033[32;1m          TOTAL A SER SACADO R${soma}\033[m')