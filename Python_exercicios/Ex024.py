#Desafio é Santo ou não

cidade = str(input('Digite o nome de uma cidade: '))

print('Essa cidade se chama Santos?\n{}'.format(cidade[:5] == 'Santo' or 'santo'))
#Ultilzei o operador in para me dar True ou False se é ou não Santo.