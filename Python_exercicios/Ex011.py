#Desafio calculo de área.

altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))

area = altura * largura

print('A área total é {:.2f}m² e você irá precisar de {:.2f} litro de tinta para pintar a área total.'.format(area, area/2))