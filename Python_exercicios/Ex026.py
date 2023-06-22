#Desafio mostre

frase = input('Digite uma frase: ')


print('A letra A aparece {} vezes na frase: {}.'.format(frase.count('a'), frase))
print('A primeira posição da letra A é : {}'.format(frase.find('a')+1))
print('A ultima posição da letra A é : {}'.format(frase.rfind('a')+1))