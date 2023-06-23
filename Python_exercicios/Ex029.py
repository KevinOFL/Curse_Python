#Desafio limite de velocidade

veloc = int(input('Digite a velocidade que você está dirigindo: '))

#Variavel para somar o valor da multa.
#veloc - 80 serve para retirar o km permitido e somar só o resto que veio acima do limite.
multa = float((veloc - 80) * 7.0)

#Sistema condicional para verificar a velocidade e aplicar a multa.
if veloc > 80:
    print('''Você acaba de tomar uma multa por estar dirigindo acima de 80Km por hora.
A multa vai custar R$7.00 por cada Km acima do permitido.
Então a multa ficou no valor de R${}'''.format(multa))
else:
    print('Tudo certo senhor, pode seguir.')