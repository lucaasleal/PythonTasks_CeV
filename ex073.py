times = ('Palmeiras', 'Grêmio', 'Atlético MG', 'Flamengo', 'Botafogo', 'Bragantino',
         'Fluminense', 'Athletico PR', 'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá',
         'Corinthians', 'Cruzeiro', 'Vasco', 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América MG')
print('+=+'*15)
print(f'Lista do Brasileirão: {times}')
print('-=-'*15)
print(f'Os 5 primeiros colocados são {times[:5]}')
print('-=-'*15)
print(f'Os quatro últimos colocados são {times[16:]}')
print('-=-'*15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=-'*15)
print(f'O Vasco está na {times.index('Vasco')+1}° posição!')