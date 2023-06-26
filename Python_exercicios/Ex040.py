#Desafio média de notas

print('=-'*40)
print('\033[7mPrograma de verificação de média\033[m')
print('=-'*40)

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = (nota1 + nota2) / 2

print('=-'*40)

if media < 5.0:
    print('''Média {:.2f}
    \033[31mREPROVADO\033[m'''.format(media))
elif media > 5.0 and media < 6.9:
    print('''Média {:.2f}
        \033[33mRECUPERAÇÃO\033[m'''.format(media))
elif media > 7.0:
    print('''Média {:.2f}
        \033[32mAPROVADO\033[m'''.format(media))

print('=-'*40)