#Aula de lista dentro de lista

galera = list()
teste = list()

teste.append('Chama')
teste.append(2)
galera.append(teste[:])

teste[0] = 'Julio'
teste[1] = 24

galera.append(teste[:])

print(galera)
# ou pode ser feito dessa forma

rapaziada = [['João', 19], ['Kevin', 20], ['Maria', 30]]
print(rapaziada)

#ultilizando for
for p in rapaziada:
    print(f'{p[0]} tem {p[1]} anso de idade.')

#Colocando dados dentro da lista

dado = list()

for c in range(0, 3):
    dado.append(input('Digite seu nome: '))
    dado.append(int(input('Digite sua idade')))
    rapaziada.append(dado[:])
    dado.clear() # A cada loop é apagado os valores do ultimo loop.

print(rapaziada)

#Mostrando idades maior que 21.
maior = menor = 0

for p in rapaziada:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        maior += 1
    else:
        print(f'{p[0]} não é mairo de idade.')
        menor += 1

print(f'Temos {maior} pessoas maiores de idade e {menor} de idade.')