n = int(input('Digite um número para ver seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
for v in range(c,0,-1):
    print('{}'.format(c), end='')
    f = f*c
    if c>1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    c-=1
print('{}'.format(f))