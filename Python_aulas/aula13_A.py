#Ultilizando for in

for c in range(6, 0, -1): #De trás pra frente.
    print(c)

for c in range(1, 6): #Laço comun.
    print(c)

for c in range(0, 10, 2): #Contando de 2 em 2.
    print(c)

for c in range(0, -10, -1): #Contando números negativos.
    print(c)

n = int(input('Digite um número: '))

for c in range(0, n+1): #Ultilizando um número que o usuário digitou como limitador.
    print(c)

#Aqui peço pro usuário digitar como o for irá se comportar
i = int(input('Digite o inicio: '))
f = int(input('Digite o fim: '))
p = int(input('Digite a quantidade de passos quer dar: '))

for c in range(i, f+1, p):
    print(c)

print('FIM')