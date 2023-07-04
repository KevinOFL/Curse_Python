#Ultilizando tuplas

lache = ('pizza', 'hamburguer', 'coxinha', 'pastel', 'pudim', 'batata frita')
outro = (1, True, 'Olá', False, 6.8)

print(lache)
print(lache[1])
print(lache[-2])
print(outro)

#Tuplas são IMUTAVEIS
#lache[1] = 'churros' = TypeError: 'tuple' object does not support item assignment
#print(lache)

for comida in lache:
    print(f'Eu vou comer {comida}')
print('Comi tudo!!')

for cont in range(0, len(lache)):
    print(lache[cont], end=' ')

del outro
print(outro) #NameError: name 'outro' is not defined