#Desafio lista completa de notas.

from math import floor
from time import sleep

print('=-'*36)
print(' '*19, '\033[7;1m - Lista completa de notas  - \033[m')
print('=-'*36)

lista = []
quant = cont = 0

while True:
    quant = int(input('Quantidade de alunos: '))

    while cont < quant:
        aux = []
        nome = input('Qual o nome do aluno: ')

        nota1 = float(input('Digite a 1ª nota do aluno (0.0 até 10.0): '))
        while nota1 > 10.0 or nota1 < 0:
            print(f'\033[31mVocê digitou uma nota inválida. Digite novamente.\033[m')
            nota1 = float(input('Digite novamente a 1ª nota do aluno (0.0 até 10.0): '))

        nota2 = float(input('Digite a 2ª nota do aluno (0.0 até 10.0): '))
        while nota2 > 10.0 or nota2 < 0:
            print(f'\033[31mVocê digitou uma nota inválida. Digite novamente.\033[m')
            nota2 = float(input('Digite novamente a 2ª nota do aluno (0.0 até 10.0): '))

        media = (nota1 + nota2) / 2
        #Adicionando os valores digitados para uma lista auxiliar.
        aux.append(nome)
        aux.append(nota1)
        aux.append(nota2)
        aux.append(floor(media))
        #Transferindo os valores pra lista original.
        lista.append(aux[:])
        cont += 1

    #Impressão do boletim com nome e media dos alunos.
    print('=-' * 36)
    print(' ' * 22, '\033[7;1m - Boletim Escolar  - \033[m')
    print('=-' * 36)
    sleep(1.5)
    for boletim in lista:
        print(f'Nome: {boletim[0]} | Média: {boletim[3]}')
        sleep(1.0)

    #Codigo para procurar as notas de algum aluno especifico cadastrado.
    while True:
        aluno = input('Digite o nome do aluno para ver as notas ou "\033[31msair\033[m" para finalizar: ')
        if aluno.lower() == 'sair':
            sleep(1)
            print('=-' * 36)
            print(' ' * 22, '\033[7;1m - Boletim Finalizado  - \033[m')
            print('=-' * 36)
            break
        encontrado = False
        for boletim in lista:
            if aluno.lower() == boletim[0].lower():
                sleep(1.5)
                print(f'Nome: \033[34m{boletim[0]}\033[m | 1ª Nota: \033[34m{boletim[1]}\033[m | 2ª Nota: \033[34m{boletim[2]}\033[m')
                encontrado = True
                break
        if not encontrado:
            sleep(1.5)
            print('Aluno não encontrado!')

    #Opção para cadastrar mais alunos.
    opcao = input('Deseja cadastrar notas para outros alunos? \033[33m(S/N)\033[m: ')
    if opcao.lower() == 'n':
        break

    lista.clear()
    cont = 0