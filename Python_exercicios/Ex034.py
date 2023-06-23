#Desafio aumento de salário

print('Para salário acima de R$1.250,00 aumento de 10% inferior ou igual aumento de 15%.')
sal = float(input('Digite seu salário'))

if sal <= 1250.00:
    print('Seu salário de R${}, passou a ser de R${}'.format(sal, sal*0.15 + sal))
else:
    aumento = sal*0.10 + sal
    print('Seu salário de R${}, passou a ser de R${}'.format(sal, aumento))