n = int(input('Primeiro termo da PA:'))
r = int(input('Digite a razão da PA:'))
c = 1
t = n
tot = 1
print(' {} ->'.format(n), end='')
while c<10:
    t = t+r
    print(' {} -> '.format(t), end='')
    c+=1
    tot +=1
    if c==10:
        v = int(input('PAUSA \nQuer mostrar mais quantos termos?'))
        if v>1:
            c=10-v
        else:
            print('Foram mostrados {} termos. FIM!'.format(tot))