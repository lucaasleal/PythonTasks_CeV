matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
totpar = terc = 0
mseg = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para {[l, c]}: '))
        if matriz[l][c]%2==0:
            totpar+=matriz[l][c]
        terc += matriz[l][2]
        if l==1 and c==0:
          mseg = matriz[l][c]
        else:
            if mseg<matriz[l][c]:
                mseg = matriz[l][c]
print('-=-'*10)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-=-'*10)
print(f'A soma dos valores pares é {totpar}.')
print(f'A soma dos valores da terceira coluna é {terc}.')
print(f'O maior valor da segunda linha é {mseg}.')
