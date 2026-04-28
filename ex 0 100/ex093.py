jogador =  dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
for c in range(0, tot):
    partidas.append(int(input(f'QUANTOS GOLS NA PARTIDA {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print(jogador)
print()
for k, v in jogador.items():
    print(f'{k}: {v}')
print()
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f' ----> Na partida {i}, fez {v} gols.')



