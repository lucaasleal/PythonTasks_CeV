print('===RODOVIÁRIA===')
d = int(input('Qual é a distância da viagem em Km?'))
if d<=200:
    print('O VALOR DA PASSAGEM É DE R${:.2f}'.format(d*0.5))
else:
    print('O VALOR DA PASSAGEM É DE R${:.2f}'.format(d*0.45))