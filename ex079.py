lista = []
resp = ''
while True:
    n = (int(input('Digite um valor: ')))
    if n not in lista:
        print('Valor adicionado com sucesso')
        lista.append(n)
    else:
        print('Valor duplicado! Não vou adicionar...')
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-=-'*20)
lista.sort()
print(f'Voce digitou os valores {lista}')

