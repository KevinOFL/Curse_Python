#Desafio descubra o número.

#Importamos a biblioteca random para gerar um número de 0 a 5
import random

#Variavel que vai receber o número sorteado
numPc = random.randint(0, 5)

print('O PC sorteou um número de 0 a 5.\nTente descobrir qual foi. ')
numUsua = int(input('Digite o número: '))

#Sistema condicional pra verificar se o usúario acertou ou não
if numUsua == numPc:
    print('''Parabéns você venceu!!
Número que você escolheu {}
Número sorteado pelo PC {}'''.format(numUsua, numPc))
else:
    print('''Você perdeu!!
Número sorteado foi {}'''.format(numPc))