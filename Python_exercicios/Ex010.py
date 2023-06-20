#Desafio contação do Dolar.
#Cotação do dia 20/06/2023 = U$4,78

valorReais = float(input('Digite quantos reais você deseja converter: '))
valorDolar = float(input('Digite quantos dolar você deseja converter: '))

print('A conversão de R${} para Dolar é U${}'.format(valorReais, valorReais/4.78))
print('A conversão de U${} para Reais é R${}'.format(valorDolar, valorDolar*4.78))