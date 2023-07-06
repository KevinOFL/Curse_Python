#Aula teoria sobre lista

num = [2, 5, 9, 1]
num[2] = 25 #Alterando um valor por outro.
print(num)

num.append(90) #Adicionando um novo valor.

num.sort() #Corrigindo ordem da lista.
print(num)

num.sort(reverse=True) #Revertendo a ordem.
print(num)

print(f'Essa lista tem {len(num)} valores.') #Mostrando quantos valores possui essa lista.

num.insert(3, 0.5) #Adicionando um valor float em um determinado indice da lista.
print(num)

del num[2]
print(num) #Removendo um determinado indice.

num.pop() #Removendo o ultimo indice.
print(num)

num.remove(25) #Removendo um valor pelo nome.
print(num)
