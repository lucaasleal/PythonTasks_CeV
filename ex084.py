pessoas = list()
dado = list()
pesado = list()
leve = list()
tot = 0
maisp = menosp = 0
while True:
    dado.append(str(input('Nome:')))
    dado.append(float(input('Peso:')))
    if len(pessoas) == 0:
        maisp = menosp = dado[1]
    else:
        if dado[1] <= menosp:
            leve.append(dado[0])
            menosp = dado[1]
        elif dado[1]>=maisp:
            pesado.append(dado[0])
            maisp = dado[1]
    pessoas.append(dado[:])
    dado.clear()
    tot+=1
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-=-'*15)
print(f'Ao todo, você cadastrou {tot} pessoas.')
print(f'O maior peso foi de {maisp}Kg. Peso de {pesado}')
print(f'O menor peso foi de {menosp}Kg. Peso de {leve}')
