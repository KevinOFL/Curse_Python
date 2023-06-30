#Desafio descubra o número.

#Importamos a biblioteca random para gerar um número de 0 a 10.
import random

#Variavel que vai receber o número sorteado v2.0
numPc = random.randint(0, 10)

print('-=-'*36)
print('''Adivinhe o número v2.0
O PC sorteou um número de 0 a 10 \nTente descobrir qual foi. ''')
print('-=-'*36)

numUsua = int(input('Digite o número: '))

print('-=-'*36)

cont = 1

#Sistema condicional de verificação, se o usuário errar ele vai tentar novamente até acerta.
while numUsua != numPc:
    numUsua = int(input('Ops, \033[33;1mvocê errou\033[m digite outro número: '))
    print('==' * 36)
    cont += 1

if numUsua == numPc:
    print('-=-' * 36)
    print('''Parabéns você venceu!!
Número que você escolheu {}
Número sorteado pelo PC {}
Número de tentaivas {}'''.format(numUsua, numPc, cont))
