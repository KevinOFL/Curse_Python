#if else

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
n3 = float(input('Digite sua terceira nota: '))

m = (n1 + n2 + n3) / 3

print('A sua média foi {:.2f}'.format(m))

if m >= 6.0:
    print('Sua nota foi ótima PARABÉNS !')
else:
    print('Sua nota foi PESSIMA!')