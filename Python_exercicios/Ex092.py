#Desafio Formulario de aposentadoria.

from datetime import date

print('=-'*36)
print(' '*18, '\033[7;1m - Formulario de aposentadoria  - \033[m')
print('=-'*36)

candidato = dict()
anoAtual = date.today().year

candidato['Nome'] = input('Digite seu nome: ')
candidato['Idade'] = anoAtual - int(input('Digite seu ano de nascimento: '))
candidato['Sexo'] = input('Qual seu sexo ? [M/F]: ')

op = input('Possui carteira de trabalho (CPTS) ? [S/N]: ')
if op.lower() == 's' or op.lower() == 'sim':
    candidato['CPTS'] = int(input('Digite a o código da sua CPTS (sem traços): '))
    candidato['Contribuição'] = anoAtual - int(input('Digite o ano de contratação: '))
    candidato['Salário'] = float(input('Digite seu salário: R$'))

print('=-'*36)

print(f''' ------- Resumo -------
Nome: {candidato['Nome']}
Idade: {candidato['Idade']}''')

if candidato.get('CPTS'):
    print(f'''Código da CPTS: {candidato['CPTS']}
Anos de contribuição: {candidato['Contribuição']}
Salário: {candidato['Salário']}''')

    if candidato['Sexo'].lower() == 'f':

        if candidato['Idade'] < 61 and candidato['Contribuição'] < 15:
            print(f'''Resultado: \033[31mAinda não é possivel se aposentar\033[m,
    falta {15 - candidato['Contribuição']} anos de contribuição e idade minima de 61 anos.''')

        elif candidato['Idade'] < 61 and candidato['Contribuição'] >= 15:
            print(f'''Resultado: \033[31mAinda não é possivel se aposentar\033[m,
    pois você não possui idade minima de 61 anos ou maior.''')

        elif candidato['Idade'] >= 61 and candidato['Contribuição'] >= 15:
            print(f'''Resultado: \033[32mJá é possivel se aposentar!\033[m''')

        elif candidato['Idade'] >= 61 and candidato['Contribuição'] < 15:
            print(f'''Resultado: \033[31mAinda não é possivel se aposentar\033[m,
    pois ainda falta {15 - candidato['Contribuição']} anos de contribuição. (Minimo é 15 anos ou mais)''')

    if candidato['Sexo'].lower() == 'm':

        if candidato['Idade'] < 65 and candidato['Contribuição'] < 15:
            print(f'''Resultado: \033[31mAinda não é possivel se aposentar\033[m,
    falta {15 - candidato['Contribuição']} anos de contribuição e idade minima de 65 anos.''')

        elif candidato['Idade'] < 65 and candidato['Contribuição'] >= 15:
            print(f'''Resultado: \033[31mAinda não é possivel se aposentar\033[m,
    pois você não possui idade minima de 65 anos ou maior.''')

        elif candidato['Idade'] >= 65 and candidato['Contribuição'] >= 15:
            print(f'''Resultado: \033[32mJá é possivel se aposentar!\033[m''')

        elif candidato['Idade'] >= 65 and candidato['Contribuição'] < 15:
            print(f'''Resultado: \033[31mAinda não é possivel se aposentar\033[m,
    pois ainda falta {15 - candidato['Contribuição']} anos de contribuição. (Minimo é 15 anos ou mais)''')

print('=-'*36)