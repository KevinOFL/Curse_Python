#Desafio M ou F.

print('=-'*36)
print(' '*32,'\033[7mM ou F\033[m')
print('=-'*36)

sexo = ''

while sexo != 'm' and sexo != 'f':
    sexo = str(input('Qual o seu sexo? [M/F]')).upper()

print('=-'*36)

print('Obrigado!')