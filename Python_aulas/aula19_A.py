#Aula sobre dicionarios em python.

from time import sleep

pessoas = {'nome': 'Kevin', 'sexo': 'M', 'idade': 20}

#Ultilizando print formatado para mostrar dados do dicionario.
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')

#Métodos sobre os valores de um dicionario.
print(pessoas.values())
print(pessoas.keys())
print(pessoas.items())

#Mesclando com for.
for k, v in pessoas.items():
    print(f'{k} = {v}')

#Mescla dicionario com lista.
brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)
#print

print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])

#Adicionando valores
estado = dict()
for c in range(0, 3):
    estado['uf'] = input('Unidade federativa: ')
    estado['sigla'] = input('Sigla do estado: ')
    brasil.append(estado.copy())
for k, v in brasil:
    print(f'O campo {k} tem valor {v}.')
    sleep(1)