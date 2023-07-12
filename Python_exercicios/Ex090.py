#Desafio situação de um aluno

from time import sleep

print('=-'*36)
print(' '*21, '\033[7;1m - Situação de um aluno  - \033[m')
print('=-'*36)

lista = list()
form = dict()
cont = 0

quant = int(input('Digite a quantidade de alunos: '))
while cont < quant:
    form['nome'] = input('Digite seu nome: ')
    form['média'] = float(input('Digite sua média: '))
    if form['média'] > 6:
        form['situação'] = '\033[32mAprovado\033[m'
    else:
        form['situação'] = '\033[31mReprovado\033[m'
    lista.append(form.copy())
    cont += 1

print('=-'*36)
print('     \033[7m - Situação dos alunos -\033[m')
print('=-'*36)
sleep(1.5)

for aluno in lista:
    print(f'''O aluno {aluno['nome']} possui uma média de {aluno['média']}.
Situação: {aluno['situação']}''')
    print('--'*36)
    sleep(1)




