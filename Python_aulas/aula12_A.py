#Aula elif

nome = input('Qual o seu nome: ')

if nome == 'Gustavo':
    print('Que nome bonito!')

elif nome == 'João' or nome == 'Pedro' or nome == 'Maria':
    print('Seu nome é bem comun no Brasil!')

elif nome in 'Ana Giovanna Jessica Raquel':
    print('Belo nome feminino!')

else:
    print('Seu nome é bem comun')
print('Tenha um bom dia {}{}{} !'.format('\033[31m',nome, '\033[m'))

print(35 / 4)