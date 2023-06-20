#Desafio do desconto.

valor = float(input('Digite o valor do produto: '))

print('Você acaba de receber 5% de desconto nesse produto que custa R${:.2f}.\nO valor dele agora é R${:.2f}'.format(valor, valor-(valor*0.05)))