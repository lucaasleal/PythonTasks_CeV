print(' Controle de Terrenos')
print('-'*23)
def area(l, c):
    tot = 0
    tot = l*c
    print(f'A área de um terreno {l}x{c} é de {tot}m².')


l = (float(input('LARGURA (m): ')))
c = (float(input('COMPRIMENTO (m): ')))
area(l, c)