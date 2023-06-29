#Desafio frase palindromo

print('=-'*36)
print(' '*27,'\033[7mFrase palindromo\033[m')
print('=-'*36)

frase = input('Digite uma frase: ').strip().upper()

auxfrase = frase.split()
auxPalavra = ''.join(auxfrase)

print('=-'*36)

#Pode se usar esse tipo de código pra ler a frase de trás pra frente sem precisar do laço for.
#inverter = auxPalavra[::-1]

inverter = ''
for letra in range(len(auxPalavra) - 1, -1, -1):
    inverter += auxPalavra[letra]

if inverter == auxPalavra:
    print('A frase {}{}{} é sim um palindromo \033[34;1m{}\033[m.'.format('\033[34;1m',auxPalavra,'\033[m',inverter))
else:
    print('A frase {}{}{} não é um palindromo \033[31;1m{}\033[m.'.format('\033[31;1m',auxPalavra,'\033[m',inverter))