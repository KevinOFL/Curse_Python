#Desafio existência de um triângulo.

l1 = float(input('Digite o primeiro lado do triângulo: '))
l2 = float(input('Digite o segundo lado do triângulo: '))
l3 = float(input('Digite o terceiro lado do triângulo: '))

if l1 + l2 > l3 and l1 + l3 > l2 :
    print('É possivel SIM existir um triângulo!')
else:
    print('NÃO é possivel existir um triângulo! ')