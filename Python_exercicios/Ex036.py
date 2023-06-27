#Desafio empréstimo bancário

print('=-'*60)
print('\033[7mAutorização de Empréstimo bancário\033[m')
print('=-'*60)

valCasa = float(input('Digite o valor da casa R$ '))
sal = float(input('Digite seu salário R$ '))
anos = int(input('Em quantos anos você irá pagar: '))

calcPrest = (valCasa / anos) / 12
calSal = sal - (sal*0.70)

print('=-'*60)

if calcPrest < calSal:
    print('''Seu empréstimo foi {}APROVADO{}!!
    Em {} parcelas de R${:.2f} cada !!'''.format('\033[32m', '\033[m',anos * 12, calcPrest ))
else:
    print('''Seu empréstimo foi {}NEGADO{}!
    O valor das parcelas R${:.2f} ultrapssou o valor de 30% do seu sálario R${:.2f} !!'''.format('\033[31m', '\033[m', calcPrest, calSal))

print('=-'*60)