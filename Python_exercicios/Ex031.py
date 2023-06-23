#Desafio preço de passagem

print('Viagens até 200Km será cobrado R$0.50 por Km, acima disso o valor vai para R$0.45.')

pas = int(input('Digite quantos Km você irá percorrer nessa viagem: '))

if pas <= 200:
    print('''Sua viagem tem {}Km então será cobrado R$0.50 para cada Km.
Ela ficou no valor de R${}'''.format(pas, float(pas * 0.50)))
else:
    print('''Sua viagem tem {}Km então será cobrado R$0.45 para cada Km.
Ela ficou no valor de R${}'''.format(pas, float(pas * 0.45)))