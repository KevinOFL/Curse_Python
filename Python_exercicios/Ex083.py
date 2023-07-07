#Desafio Expressão OK!

print('=-'*36)
print(' '*25,'\033[7;1m - Expressão OK!  - \033[m')
print('=-'*36)

pilha = []

expressao = input("Digite uma expressão com parênteses: ")

for caractere in expressao:
    if caractere == '(':
        pilha.append(caractere)
    elif caractere == ')':
        if len(pilha) == 0:
            pilha.append(caractere)
            break
        else:
            pilha.pop()

print('=-'*36)

if len(pilha) == 0:
    print("A expressão está correta.")
else:
    print("A expressão está incorreta.")

print('=-'*36)