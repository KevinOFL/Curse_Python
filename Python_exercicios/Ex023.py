#Desafio 0 a 9999

num = input('Digite um número inteiro de 0 a 9999: ')
numInt = int(input('Digite um número inteiro de 0 a 9999: '))

print('''Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}'''.format(num[3], num[2], num[1], num[0]))
#Ultilizei o fatiamento para pegar cada indice e mostrar.

#Aqui temos uma versão do desafio só que com números inteiros.

u = numInt // 1 % 10 #Calculo para pegar a unidade de um valor até 9999
d = numInt // 10 % 10 #Calculo para pegar a dezena de um valor até 9999
c = numInt // 100 % 10 #Calculo para pegar a centena de um valor até 9999
m = numInt // 1000 % 10 #Calculo para pegar a milhar de um valor até 9999

print('''Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}'''.format(u, d, c, m))
