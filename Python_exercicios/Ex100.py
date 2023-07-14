#Desafio Sorteio e Soma pares

# Packages imports
from random import sample

# Funções
def apresentação():
    print('=-'*80)
    print(' '*61, '- Sorteio e Soma pares -')
    print('=-'*80)
def linha():
    print('--'*80)
def sorteio():
    sorteados = sample(range(0, 100), 5)
    return sorteados
def somarPar(lst):
    soma = 0
    for somando in lst:
        if somando % 2 == 0:
            soma += somando
    return soma

# Programa principal

apresentação()

números_sorteados = sorteio()

print('          - RESULTADO -')
linha()
print(f'''O sorteio foi de 0 a 100.
Os números sorteados foram {números_sorteados}.
A soma dos valores pares do sorteio foi {somarPar(números_sorteados)}.''')

linha()