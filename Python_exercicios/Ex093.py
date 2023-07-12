#Desafio Expecificações de jogador

print('=-'*36)
print(' '*18, '\033[7;1m - Expecificações de jogador  - \033[m')
print('=-'*36)

jogos = dict()
gols = 0
c = 1


jogos['nome'] = input('Digite o nome do jogador: ')
jogos['partidas'] = int(input('Quantas partidas ele jogou nessa temporada: '))


for c in range(1, jogos['partidas']+1):
    chave = f'partida {c}'
    valor = int(input(f'Quantos gol marcou na {c}ª partida: '))
    jogos[chave] = valor
    gols += valor

print('=-'*36)

print(f' ---------- \033[7;32;1m Estátistica do Jogador - {jogos["nome"]} \033[m ----------')

print(f'''Nome: \033[32m{jogos['nome']}\033[m
Partidas jogadas: \033[32m{jogos['partidas']}\033[m
 ---------- Resumo do jogador ----------''')
for chave, valor in jogos.items():
    if chave.startswith('partida '):
        print(f'{chave}: {valor} gols')
        print('--'*36)
print('Média de gols por partida: \033[32m{:.1f}\033[m'.format(gols/jogos['partidas']))

print('=-'*36)
