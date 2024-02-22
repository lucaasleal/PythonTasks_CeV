dados = {}
gols = list()
tot = p = 0
dados['Nome'] = str(input('Nome do Jogador: '))
n = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
for c in range(1, n+1):
    gols.append(int(input(f'Quantos gols na partida {c}:')))
dados['Gols'] = gols
for i, v in enumerate(gols):
    tot += v
print('-=-'*10)
print(f'O jogador {dados['Nome']} jogou {n} partidas.')
for i, v in enumerate(gols):
    print(f'   => Na partida {i+1}, fez {v}')
print(f'Foi um total de {tot} gols.')

