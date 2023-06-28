#Desafio números pares.

print('=-'*36)
print(' '*28,'\033[7mNúmeros par\033[m')
print('=-'*36)

for c in range(2, 50+1, 2):
    print('Número par {}{}{}'.format('\033[32;1m',c,'\033[m'))