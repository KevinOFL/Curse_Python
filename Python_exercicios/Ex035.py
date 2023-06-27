#Desafio existência de um triângulo.

print('-=-' * 60)
print('Análise de Triângulo')
print('-=-' * 60)

l1 = float(input('Digite o primeiro lado do triângulo: '))
l2 = float(input('Digite o segundo lado do triângulo: '))
l3 = float(input('Digite o terceiro lado do triângulo: '))

if l1 + l2 > l3 and l1 + l3 > l2 :
    print('-=-' * 60)
    print('1º Lado: {:.2f}'.format(l1))
    print('2º Lado: {:.2f}'.format(l2))
    print('3º Lado: {:.2f}'.format(l3))
    print('É possivel SIM existir um triângulo!')
    print('-=-' * 60)
else:
    print('-=-' * 60)
    print('1º Lado: {:.2f}'.format(l1))
    print('2º Lado: {:.2f}'.format(l2))
    print('3º Lado: {:.2f}'.format(l3))
    print('NÃO é possivel existir um triângulo! ')
    print('-=-' * 60)