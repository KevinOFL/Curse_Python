#Desafio nome dissecado

nome = input('Digite seu nome completo: ')

#Vou transformar todas as letras em maiusculas
print(nome.upper())

#Vou trasnformar todas as letras em minusculas
print(nome.lower())

#Variavel para armazenar a nova frase sem os espaços
nomeSemEspaço = nome.replace(' ', '')
print(len(nomeSemEspaço))

#Dividindo a frase e armazenando os novos indices em outra variavel.
primeiroNome = nome.split()
print(len(primeiroNome[0]))
