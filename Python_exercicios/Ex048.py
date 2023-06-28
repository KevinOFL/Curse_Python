#Desafio núemros impar, multiplos de 3.

print('=-'*36)
print(' '*16,'\033[7mSoma de Números impar multiplos de 3\033[m')
print('=-'*36)

soma = 0

for c in range(0, 500+1, 3):
    if c % 2 == 1:
        soma += c

# for c in range(0, 501):
#     if c % 2 != 0 and c % 3 == 0:
#          soma += c

print('Total da soma desses números: {}{}{}'.format('\033[32;1m', soma, '\033[m'))