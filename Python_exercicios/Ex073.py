#Desafio campeonato brasileiro de futebol

print('=-'*36)
print(' '*18,'\033[7;1m Campeonato brasileiro de futebol \033[m')
print('=-'*36)

times_brasileirao = ("Flamengo", "Internacional", "Atlético Mineiro", "São Paulo",
"Fluminense", "Grêmio", "Palmeiras", "Santos", "Athletico Paranaense", "Bragantino",
"Chapecoense", "Corinthians", "Atlético Goianiense", "Bahia", "Sport Recife", "Fortaleza",
"Vasco da Gama", "Goiás", "Coritiba", "Botafogo")

print(f'''\033[34mOs times em ordem alfabetica\033[m:
{sorted(times_brasileirao)}''')

print('-'*60)

print(f'''Os \033[34m5\033[m primeiros colcoados:
{times_brasileirao[0:5]}''')

print('-'*60)

print(f'''Os \033[34m4\033[m ultimos colcoados:
{times_brasileirao[16:]}''')

print('-'*60)

print(f'''O time da Chapecoense está na posição \033[34m{times_brasileirao.index('Chapecoense')+1}º lugar\033[m na tabela.''')

print('=-'*36)