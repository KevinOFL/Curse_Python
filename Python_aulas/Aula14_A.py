#Aula sobre while

#for c in range(1, 10):
#    print(c)
#print('FIM')

c = 1
while c < 10:
    print(c)
    c+=1
print('FIM')

r = 'S'
while r == 'S':
    n = int(input('Digite um número: '))
    r = input('Quer continuar ? [S/N]').upper()
print('FIM')

num = 1
par = impar = 0

while num != 0:
    num = int(input('Digite um valor: '))
    if num != 0:
        if num % 2 == 0:
            par += 1
        else:
            impar += 1

print('Você digitou {} números pares e {} números impares.'.format(par, impar))