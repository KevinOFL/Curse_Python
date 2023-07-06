#Desafio Vários valores numéricos.

print('=-'*36)
print(' '*19,'\033[7;1m - Vários Valores numéricos  - \033[m')
print('=-'*36)

valores = list()
num = 0

while True:
    num = input("Digite um valor numérico (ou 'sair' para encerrar): ")

    if num.lower() == 'sair':
        break

    if num.isdigit():
        num = int(num)
        if num not in valores:
            valores.append(num)
    else:
        print("Valor inválido. Digite apenas valores numéricos.")

valores.sort()

print("Valores únicos digitados, em ordem crescente:")
for valor in valores:
    print(valor, end=' - ')