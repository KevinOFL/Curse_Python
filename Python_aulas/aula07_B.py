#ULtilizando operadores aritimeticos

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))

s = n1 + n2
sb = n1 - n2
m = n1 * n2
d = n1 / n2
p = n1 ** n2
di = n1 // n2
r = n1 % n2

print('A soma é {}, o produto é {}, e a divisão é {}'.format(s, m, d), end='><')
print('Divisão inteira {} e pôtencia {}'.format(di, p))
