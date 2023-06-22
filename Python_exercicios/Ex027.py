#Desafio primeiro e ultimo nome.

nome = input('Digite seu nome completo: ')

#Ultilizei o split() para criar indice de cada palavra
nomeSeparado = nome.split()

#E depois peguei o indice 0 onde seria o primeiro nome.
#E -1 que ai ele iria pegar o ultimo pois iria vim de tras pra frente a leitura dos indice.
print('O primeiro nome é {} e o ultimo nome seria esse {}.'.format(nomeSeparado[0], nomeSeparado[-1]))