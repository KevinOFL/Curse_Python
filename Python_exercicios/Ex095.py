#Desafio Expecificações de jogador v2.0

print('=-'*36)
print(' '*18, '\033[7;1m - Expecificações de jogador 2.0  - \033[m')
print('=-'*36)

lista = list()
gols = 0
c = 1

while True:
    opc = input('Deseja adicionar algum jogador? "\033[33m[S/N]\033[m" :')
    if opc.lower() == 'n':
        break

    while True:
        jogos = dict()
        jogos['nome'] = input('Digite o nome do jogador: ')
        jogos['partidas'] = int(input('Quantas partidas ele jogou nessa temporada: '))

        for c in range(1, jogos['partidas']+1):
            chave = f'partida {c}'
            valor = int(input(f'Quantos gol marcou na {c}ª partida: '))
            jogos[chave] = valor
            gols += valor

        lista.append(jogos)
        break

    print('=-'*36)

for jogador in lista:
    nome = jogador['nome']
    gols = ', '.join(str(jogador[chave]) for chave in jogador if chave != 'nome' and chave != 'partidas')
    total_gols = sum(jogador[chave] for chave in jogador if chave != 'nome' and chave != 'partidas')

    print(f' ---------- \033[7;32;1m Resumo do Jogador - {nome} \033[m ----------')
    print(f'Nome: \033[32m{nome}\033[m | Gols em partidas: \033[32m{gols}\033[m | Total na temporada: \033[32m{total_gols}\033[m')
    print('--'*36)

while True:
    opc = input('Digite o nome do jogador que deseja ver as estatistica. "\033[33mOu digite sair para finalizar\033[m" :')
    if opc.lower() == 'sair':
        break

    for jogador in lista:
        if jogador['nome'] == opc:
            nome = jogador['nome']
            partidas = jogador['partidas']
            gols_partidas = [jogador[chave] for chave in jogador if chave.startswith('partida ')]
            totalGols = sum(gols_partidas)

            print(f' ---------- \033[7;32;1m Estatísticas do Jogador - {nome} \033[m ----------')
            print(f'Nome: \033[32m{nome}\033[m | Partidas jogadas: \033[32m{partidas}\033[m')
            print(f'Gols em cada partida: \033[32m{", ".join(str(g) for g in gols_partidas)}\033[m')
            print(f'Total de gols na temporada: \033[32m{total_gols}\033[m')
            print('Média de gols por partida: \033[32m{:.1f}\033[m'.format(total_gols / partidas))
            print('--' * 36)
            break
        else:
            print('Jogador não encontrado.')

print('=-'*36)