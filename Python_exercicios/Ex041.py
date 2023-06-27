#Desafio categoria de natação

from datetime import date

print('=-'*40)
print('\033[7mPrograma colocação de categoria\033[m')
print('=-'*40)

anoNasc = int(input('Digite seu ano de nascimento: '))

anoAtual = date.today().year
calcIdade = anoAtual - anoNasc

print('=-'*40)

if calcIdade <= 9:
    print('''Você possui {} anos
    Sua categoria é {}MIRIM{}'''.format(calcIdade, '\033[36;1m', '\033[m'))
elif calcIdade > 9 and calcIdade <= 14:
    print('''Você possui {} anos
        Sua categoria é {}INFANTIL{}'''.format(calcIdade, '\033[34;1m', '\033[m'))
elif calcIdade > 14 and calcIdade <= 19:
    print('''Você possui {} anos
        Sua categoria é {}JUNIOR{}'''.format(calcIdade, '\033[32;1m', '\033[m'))
elif calcIdade > 19 and calcIdade <= 20:
    print('''Você possui {} anos
        Sua categoria é {}SÊNIOR{}'''.format(calcIdade, '\033[33;1m', '\033[m'))
elif calcIdade > 20:
    print('''Você possui {} anos
        Sua categoria é {}MASTER{}'''.format(calcIdade, '\033[31;1m', '\033[m'))

print('=-'*40)