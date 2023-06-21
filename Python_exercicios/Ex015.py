#Desafio aluguel de carro.

km = float(input('Digite a quantidade de Km rodados: '))
dias = int(input('Digite a quantidade de dias alugado: '))

#Posso gerar tanto 2 variaveis para calcular cada valor ou...
somaDias = dias * 60.00
somaKm = km * 0.15

#Gerar uma única variavel para o total.
#total = (dias * 60.00) + (km * 0.15)

print('Você rodou com o carro {:.2f}Km por {} dia/s'.format(km, dias))
print('Sua fatura total do aluguel é R${:.2f}'.format(somaDias+somaKm))