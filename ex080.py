lista = []
for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c==0 or n > lista[-1]:
        print('Adicionado ao final da lista...')
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <=lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-=-'*15)
print(f'Os valores digitados foram {lista}')