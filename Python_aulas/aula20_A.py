#Aula sobre funções (def) com e sem paramétros

# Empacotador ou desempacotador
# Quando colocamos asterisco "*" ao lado do parametro, significa
# que estamos falando pro Python que não sabemos quantos parámetros viram para a função.
def contador(*n):
    for valor in n:
        total = len(n)
        print(f'Valores recebidos {valor}')
    print(f'Total {total}')

# Função para dobrar valores de uma lista
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print(lst)

def multiplicacao(a, b):
    return  a * b

def linhas():
    print('--'*36)

def saudacao(nome):
    print("Olá, " + nome + "! Bem-vindo(a).")

# Chamando a função
saudacao("Alice")
linhas()
def soma(a, b):
    return a + b

# Chamando a função e armazenando o resultado em uma variável
resultado = soma(3, 5)
print(resultado)  # Saída: 8

linhas()

# Ultilizando input como parametro
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))

print(multiplicacao(n1, n2))

# ultiliando o desempacotador
contador(7,8,6,9,2,3)

lst1 = [1,8,5,2,558,8,63]
lst2 = [8,-5,-65,52,9,8.8,99.5]

dobra(lst1)
dobra(lst2)