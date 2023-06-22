#Desafio 0 a 9999

num = input('Digite um número inteiro de 0 a 9999: ')

print('''Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}'''.format(num[3], num[2], num[1], num[0]))
#Ultilizei o fatiamento para pegar cada indice e mostrar.