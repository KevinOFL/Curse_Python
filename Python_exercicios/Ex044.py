#Desafio Pagamento avista ou parcelado.

print('=-'*36)
print(' '*19,'\033[7mPrograma - calculo de pagamento\033[m')
print('=-'*36)

precProdu = float(input('Digite o preço do produto R$'))
condPag = int(input('''Escolha a forma de pagamento
1 - Á vista dinheiro/cheque 10% de desconto
2 - À vista no cartão 5% de desconto
3 - em até 2x no cartão preço normal
4 - 3x ou mais no cartão 20% de juros
Escolha a opção desejada: '''))

print('=-'*36)

if condPag == 1:
    print('''\033[7mTOTAL A PAGAR\033[m
    Valor do produto R${}
            +
    Desconto de 10%
    
    \033[34;1mTOTAL R${}\033[m'''.format(precProdu, precProdu - (precProdu*0.10)))
elif condPag == 2:
    print('''\033[7mTOTAL A PAGAR\033[m
        Valor do produto R${}
                +
        Desconto de 5%

        \033[32;1mTOTAL R${}\033[m'''.format(precProdu, precProdu - (precProdu * 0.05)))
elif condPag == 3:
    print('''\033[7mTOTAL A PAGAR\033[m

        \033[33;1mTOTAL 2x de R${}\033[m'''.format(precProdu / 2))
elif condPag == 4:
    print('''\033[7mTOTAL A PAGAR\033[m
        Valor do produto R${}
                +
        Juros de 20%

        \033[33;1mTOTAL 3x de R${}\033[m'''.format(precProdu, (precProdu + (precProdu * 0.20)) / 3))
else:
    print('\033[31;1mOpção {} IVÁLIDA, tente novamente!!\033[m'.format(condPag))