#Desafio jokênpo

from random import randint
from time import sleep

op = ('PEDRA', 'PAPEL', 'TESOURA')

pc = randint(0, 2)

print('=-'*36)
print(' '*30,'Jokênpo')
print('=-'*36)

us = int(input('''Qual a sua jogada: 
0 - PEDRA
1 - PAPEL
2 - TESOURA
Digite a opção: '''))

print('=-'*36)

print('\033[34;1mJO\033[m')
sleep(0.5)
print('   \033[32;1mKÊN\033[m')
sleep(0.5)
print('       \033[35;1mPO\033[m')
sleep(0.5)

print('=-'*36)

if pc == 0:
    if us == 0:
        print('O computador jogou {}{}{}'.format('\033[34;1m',op[pc],'\033[m'))
        print('O usuário jogou {}{}{}'.format('\033[34;1m', op[0], '\033[m'))
        print('=-'*36)
        print('''\033[7;1mRESULTADO\033[m
                \033[33;1mEMPATE!\033[m''')
    elif us == 1:
        print('O computador jogou {}{}{}'.format('\033[34;1m', op[pc], '\033[m'))
        print('O usuário jogou {}{}{}'.format('\033[32;1m', op[1], '\033[m'))
        print('=-'*36)
        print('''\033[7;1mRESULTADO\033[m
                \033[32;1mUSUÁRIO VENCEU!\033[m''')
    elif us == 2:
        print('O computador jogou {}{}{}'.format('\033[34;1m', op[pc], '\033[m'))
        print('O usuário jogou {}{}{}'.format('\033[35;1m', op[2], '\033[m'))
        print('=-' * 36)
        print('''\033[7;1mRESULTADO\033[m
                \033[32;1mCOMPUTADOR VENCEU!\033[m''')
    else:
        print('\033[31;1mOPÇÃO INVÁLIDA\033[m')

elif pc == 1:
    if us == 0:
        print('O computador jogou {}{}{}'.format('\033[32;1m',op[pc],'\033[m'))
        print('O usuário jogou {}{}{}'.format('\033[34;1m', op[0], '\033[m'))
        print('=-'*36)
        print('''\033[7;1mRESULTADO\033[m
                \033[32;1mCOMPUTADOR VENCEU!\033[m''')
    elif us == 1:
        print('O computador jogou {}{}{}'.format('\033[32;1m', op[pc], '\033[m'))
        print('O usuário jogou {}{}{}'.format('\033[32;1m', op[1], '\033[m'))
        print('=-'*36)
        print('''\033[7;1mRESULTADO\033[m
                \033[33;1mEMPATE!\033[m''')
    elif us == 2:
        print('O computador jogou {}{}{}'.format('\033[32;1m', op[pc], '\033[m'))
        print('O usuário jogou {}{}{}'.format('\033[35;1m', op[2], '\033[m'))
        print('=-' * 36)
        print('''\033[7;1mRESULTADO\033[m
                \033[32;1mUSUÁRIO VENCEU!\033[m''')
    else:
        print('\033[31;1mOPÇÃO INVÁLIDA\033[m')

elif pc == 2:
    if us == 0:
        print('O computador jogou {}{}{}'.format('\033[35;1m',op[pc],'\033[m'))
        print('O usuário jogou {}{}{}'.format('\033[34;1m', op[0], '\033[m'))
        print('=-'*36)
        print('''\033[7;1mRESULTADO\033[m
                \033[32;1mUSUÁRIO VENCEU!\033[m''')
    elif us == 1:
        print('O computador jogou {}{}{}'.format('\033[35;1m', op[pc], '\033[m'))
        print('O usuário jogou {}{}{}'.format('\033[32;1m', op[1], '\033[m'))
        print('=-'*36)
        print('''\033[7;1mRESULTADO\033[m
                \033[32;1mCOMPUTADOR VENCEU!\033[m''')
    elif us == 2:
        print('O computador jogou {}{}{}'.format('\033[35;1m', op[pc], '\033[m'))
        print('O usuário jogou {}{}{}'.format('\033[35;1m', op[2], '\033[m'))
        print('=-' * 36)
        print('''\033[7;1mRESULTADO\033[m
                \033[33;1mEMPATE!\033[m''')
    else:
        print('\033[31;1mOPÇÃO INVÁLIDA\033[m')

print('=-' * 36)