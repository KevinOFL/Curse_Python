#Desafu=io nome, idade e sexo

print('=-'*36)
print(' '*25,'\033[7mNome, idade e sexo\033[m')
print('=-'*36)

maior = 0
femIdade = 0
soma = 0

for c in range(0, 4):
    print('-=-=-={}ª PESSOA=-=-=-'.format(c))
    nome = input('Digite seu nome: ')
    idade = int(input('Digite a sua idade: '))
    sexo = int(input('''Qual seu sexo:
    0 - Masculino
    1 - Feminino
    '''))

    soma += idade
    salvaNome = 0

    if idade > maior and sexo == 0:
        maior = idade
        salvaNome = nome

    if idade < 20 and sexo == 1:
        femIdade += 1

print('''A média de idade do grupo {:.2f}
O homem mais velho é o {} com {} anos
{} mulheres possum menos de 20 anos.'''.format(soma/4, salvaNome, maior, femIdade))
