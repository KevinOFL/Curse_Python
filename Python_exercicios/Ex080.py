#Desafio posição correta.

print('=-'*36)
print(' '*24,'\033[7;1m - Posição correta  - \033[m')
print('=-'*36)

lista = list()
num = 0

for i in range(5):
    num = int(input("Digite um valor numérico: "))
    if len(lista) == 0:
        lista.append(num)
    else:
        for j in range(len(lista)):
            if num < lista[j]:
                lista.insert(j, num)
                break
            else:
                lista.append(num)

print("Lista ordenada:")
for valor in lista:
    print(valor)
