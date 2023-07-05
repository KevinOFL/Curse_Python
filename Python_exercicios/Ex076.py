#Desafio tabela de produtos e preço.

print('=-'*36)
print(' '*26,'\033[7;1m - Tabela de preços  - \033[m')
print('=-'*36)

tupla_produtos = (
    ("Doritos ", 10.99),
    ("Trakinas ", 5.99),
    ("Farinha temperada ", 7.50),
    ("RedBull ", 15.99),
    ("Vinho ", 12.49),
    ("Coca-Cola ", 9.99),
    ("Fanta ", 8.75),
    ("Fini ", 6.99),
    ("Doce de leite ", 11.25),
    ("Paulaner ", 14.50),
)
nome = tupla_produtos[0][0]
preço = tupla_produtos[0][1]

for c in tupla_produtos:
    nome = c[0]
    preço = c[1]
    print(f'{nome:.<30}R${preço:>7.2f}')

print('=-'*36)