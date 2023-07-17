#Desafio Biblioteca de notas

# Packages imports
from time import sleep
from math import floor

# Funções
def apresentação():
    """-> Função tipo print de aresentação de titulo do programa"""
    print('=-'*80)
    print(' '*61, '- Biblioteca de notas -')
    print('=-'*80)

def linha():
    """-> Função tipo print de linhas para customização do programa."""
    print('--'*80)

def notas():
    """Função notas serve para forma um dicionario para cada aluno
    e logo no final coloca dentro de uma lista_alunos.
    Quando o usuário digitar sair será retornado uma lista de todos os alunos adicionados.
    """
    lista_alunos = []
    while True:
        aluno = {}
        aluno['nome'] = input('''Para finalizar a adição de alunos digite "\033[31msair\033[m".
Digite o nome do aluno: ''')
        if aluno['nome'].lower() == 'sair':
            break
        aluno['nota'] = float(input('Digite a nota do aluno: '))
        if aluno['nota'] > 6:
            aluno['situação'] = '\033[32mAprovado\033[m'
        else:
            aluno['situação'] = '\033[31mReprovado\033[m'
        lista_alunos.append(aluno)
    return lista_alunos

def maMeMed(sala):
    """Função maMeMed serve para pegar cada dado dentro do dicionario de cada aluno da lista.
    :param sala: lista que será percorrida.
    no final é retornado:
    maior -> Maior nota.
    menor -> Menor nota.
    media -> Média baseada no total de cadastro e notas.
    cont -> Quantidade de cadastros.
    nomeMe -> Nome da pessoa que obteve a menor nota.
    nomeMa -> Nome da pessoa que obteve a maior nota.
    """
    cont = total = 0
    menor = maior = None
    nomeMe = nomeMa = None

    for dados in sala:
        nota = dados.get('nota')
        if nota is not None:
            cont += 1
            total += nota

            if menor is None and maior is None:
                menor = nota
                maior = nota
                nomeMe = dados['nome']
                nomeMa = dados['nome']
            elif nota < menor:
                menor = nota
                nomeMe = dados['nome']
            elif nota > maior:
                maior = nota
                nomeMa = dados['nome']

    media = total / cont if cont > 0 else 0

    return maior, menor, floor(media), cont, nomeMe, nomeMa

# Programa principal

apresentação()

lista = notas()
notaMa, notaMe, notaMed, quanti, nomeMe, nomeMa = maMeMed(lista)

print('      - Analisando Dados... -')
sleep(2)
linha()
print('      - RESULTADO -')
linha()

print(f'''Qauntidade de alunos cadastrados {quanti}.
A maior nota foi de {nomeMa} com a nota {notaMa}.
A menor nota foi de {nomeMe} com a nota {notaMe}.
A média da turma foi {notaMed}.''')
linha()

print('''A situação de cada aluno: 
| Aluno  | Nota | Situação |''')
linha()

for dados in lista:
    aluno = dados['nome']
    nota = dados['nota']
    situacao = dados['situação']
    print(f'| {aluno} | {nota} | {situacao} |')

linha()