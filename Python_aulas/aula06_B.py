n = float(input('Digite um núemro: '))
print(n)
print(type(n))

n1 = input('Digite algo: ') #Digitar 4
n2 = input('Digite algo: ') #Digitar abc
n3 = int(input('Digite algo: ')) #Digitar 676
n4 = int(input('Digite algo: ')) #Digitar zzz

print(n1.isnumeric()) #Aqui irá dar True.
print(n2.isnumeric()) #Aqui irá dar False.
print(n3.isnumeric()) #Aqui irá dar AttributeError.
print(n4.isnumeric()) #Aqui irá dar ValueError.