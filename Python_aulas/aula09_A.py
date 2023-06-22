#Fatiamento

frase = 'Curso em video Python'

print(frase[3])
#Ele vai indentificar dentro da cadeia de caracteres o indice 3.

print(frase[9:13])
#9 e o indice que ele vai iniciar e vai até o indice 13 mas o 13 ele vai excluir.

print(frase[9:21])
#Ele só vai até onde é possivel ir com os caracteres da String ele não vai trazer um valor que não existe.

print(frase[9:21:2])
#9 é o inicio, 21 é o fim e o 2 e o valor que ele vai pular ele pega um indice e pula 2 sucessivamente até finalizar.

print(frase[:7])
#Como nao possui indice de inicio ele vai começar do indice 0 e vai finalizar no indice final mencionado.

print(frase[2:])
#Mesma linha de raciocinio ele tem o indice de inicio e não tem o indice final então no caso ele vai até o indice final.

print(frase[:])
#Aqui não possui nenhum tipo de indice então ele simplesmente vai mostrar a string inteira.

print(frase[9::3])
#Mesmo raciocinio quando tem 3 fatores, ele tem o indice inical, mas não tem o indice final e o 3º ele tem o indice de pulo
#no caso ele vai começar no 9 e pular de 3 em 3 até chegar no ultimo indice.