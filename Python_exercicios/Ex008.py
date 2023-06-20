#Desafio conversão de metros

valor = float(input('Digite um valor em metros que deseja converter: '))

print('O valor {:.2f}m, convertido para cemtimetros é {:.2f}cm\ne milimetros é {:.2f}mm'.format(valor, valor*100, valor*1000))