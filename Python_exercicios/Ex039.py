#Desafio Alistamento

from datetime import date

print('=-'*60)
print('\033[7mPrgrama de verificação de alistamento militar\033[m')
print('=-'*60)

anoNasc = int(input('Digite seu ano de nascimento: '))
anoHoje = date.today().year

calcAno = anoHoje - anoNasc
faltaIdade = 17 - calcAno

print('=-'*60)

if calcAno == 17 or calcAno == 18:
    print('''Você possui {} anos.
    {}Já está na hora de se ALISTAR!{}'''.format(calcAno, '\033[34m', '\033[m'))
elif calcAno < 17:
    print('''Você possui {}  anos.
    {}Ainda falta {} anos para você poder se ALISTAR!{}'''.format(calcAno, '\033[32m', faltaIdade, '\033[m'))
else:
    print('''Você possui {} anos.
        {}Já se passou {} anos da idade limite para se ALISTAR!{}'''.format(calcAno, '\033[31m', calcAno-18, '\033[m'))

print('=-'*60)