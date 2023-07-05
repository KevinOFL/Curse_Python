#Desafio Contando vogais em tupla

print('=-'*36)
print(' '*26,'\033[7;1m - Contando vogais  - \033[m')
print('=-'*36)

tupla_palavras = ("gato", "casa", "sol", "carro", "amarelo", "banana", "verde", "praia", "computador", "livro")

for p in tupla_palavras:
    print(f'\nna palavra \033[33;1m{p}\033[m temos como vogais:  ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'\033[31;1m{letra}\033[m', end=' ')

print('=-'*36)