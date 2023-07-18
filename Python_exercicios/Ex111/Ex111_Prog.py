# Desafio Trabalhando com modulos 5.

from ultilidades.moeda import resumo
import Ex111_func

Ex111_func.apresentação()

n = float(input('Digite um número: R$'))
t = int(input('Digite a taxa: '))

resumo(n, t)


