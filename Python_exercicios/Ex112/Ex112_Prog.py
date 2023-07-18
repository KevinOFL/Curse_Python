# Desafio Trabalhando com modulos 5.

from ultilidades.moeda import resumo
from ultilidades.dado import leiaDinheiro
import Ex112_func

Ex112_func.apresentação()

n = leiaDinheiro('Digite um número: R$')

t = int(input('Digite a taxa: '))

resumo(n, t)


