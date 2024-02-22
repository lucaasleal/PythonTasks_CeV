tot = pmil = vb = cont = 0
nome = barato = r = ''
print('-'*30)
print('LOJA BARATUDA')
print('-'*30)
while True:
    nome = str(input('Nome do produto: '))
    valor = float(input('Preço:R$'))
    tot += valor
    cont+=1
    if valor > 1000:
        pmil += 1
    if cont == 1:
        barato = nome
        vb = valor
    else:
        if vb > valor:
            barato = nome
    resp = ' '
    while resp not in "SN":
        resp = str(input('Quer Continuar?[S/N]')).strip().upper()[0]
    if resp =='N':
        break
print('----------FIM DO PROGRAMA----------')
print(f'O total da compra foi R${tot:.2f}')
print(f'Temos {pmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${vb:.2f}')

