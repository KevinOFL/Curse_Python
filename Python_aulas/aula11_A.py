#Aula de formatação de cores do terminal
import colorsys

#1º
print('\033[1;31;43mOlá Mundo!\033[m')

#2º
a = 5
b = 8
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!'.format(a, b))

#3º
nome = 'Kevin'
print('Olá, muito prazer em te conhecer {}{}{} !!'.format('\033[35;4m',nome,'\033[m'))

#4º
cores = {'limpa':'\033[m', 'azul':'\033[34m', 'amarelo':'\033[33m', 'pretoebranco':'\033[7;30m'}
print('Olá, seja muito bem vindo a aula de formatação de cores {}{}{} !'.format( cores['pretoebranco'], nome, cores['limpa']))