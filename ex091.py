from random import randint
from time import sleep
from operator import itemgetter
jogo = {}
ranking = list()
print('Valores Sorteados:')
for c in range(1,5):
    jogo[f'jogador{c}'] = randint(1,6)
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
print('Ranking dos Jogadores:')
ranking = sorted(jogo.items(), key = itemgetter(1), reverse = "True")
for i,v in enumerate(ranking):
    print(f'{i+1}°lugar: {v[0]} com {v[1]}.')
    sleep(1)

