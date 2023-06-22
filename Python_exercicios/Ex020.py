#Desafio alternado do apagar a lousa.

import random

#from random import shuffle

a1 = str(input('Digite o nome de um aluno: '))
a2 = str(input('Digite o nome de um aluno: '))
a3 = str(input('Digite o nome de um aluno: '))
a4 = str(input('Digite o nome de um aluno: '))

alunos = [a1, a2, a3, a4]

random.shuffle(alunos)

print('A ordem de apresentação será: \n {}'.format(alunos))