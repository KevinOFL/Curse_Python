#Desafio existência de um triângulo 2.

print('=-'*35)
print('\033[7mPrograma de verificação de triângulo 2.0\033[m')
print('=-'*35)

l1 = float(input('Digite o 1º lado do triângulo: '))
l2 = float(input('Digite o 2º lado do triângulo: '))
l3 = float(input('Digite o 3º lado do triângulo: '))

print('=-'*35)

if l1 + l2 > l3 and l1 + l3 > l2 :
    print('1º Lado: {:.2f}'.format(l1))
    print('2º Lado: {:.2f}'.format(l2))
    print('3º Lado: {:.2f}'.format(l3))
    print('\033[32;1mÉ possivel SIM existir um triângulo!\033[m')
    print('=-'*35)

    if l1 == l2 == l3:
        print('\033[34;1mTriângulo equilátero\033[m')
    elif l1 == l2 != l3 or l2 == l3 != l1 or l3 == l1 != l2:
        print('\033[35;1mTriângulo isóceles\033[m')
    else:
        print('\033[36;1mTriângulo escaleno\033[m')

else:
    print('1º Lado: {:.2f}'.format(l1))
    print('2º Lado: {:.2f}'.format(l2))
    print('3º Lado: {:.2f}'.format(l3))
    print('\033[31;1mNÃO é possivel existir um triângulo!\033[m')

print('=-'*35)