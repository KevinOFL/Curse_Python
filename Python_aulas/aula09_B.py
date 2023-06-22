#Análisando, transformando e divindo String

frase = 'Curso em video Python'

#print com 3 aspas para textos longo.
print('''A Way with Words is a radio show and podcast that features
light-hearted conversation about language change, debates,
and differences, as well as new words, old sayings, slang,
family expressions, word origins and histories, etymology,
linguistics, regional dialects, word games and puzzles,
grammar, books, literature, writers and writing, and more.''')

#count() com junção upper()
print(frase.upper().count('O'))

#len() e strip()
print(len(frase.strip()))
print(len(frase))

#replace()
print(frase.replace('Python', 'JavaSc'))






