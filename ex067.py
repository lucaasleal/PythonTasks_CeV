n = 0
c=1
while True:
    n = int(input('Digite um número pra ver a tabuada:'))
    print('-=-' * 10)
    if n < 0:
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
    print('-=-'*10)
print('ERRO! Você inseriu um número Negativo!')
