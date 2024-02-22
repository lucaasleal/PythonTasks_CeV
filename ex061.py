n = int(input('Primeiro termo da PA:'))
r = int(input('Digite a razão da PA:'))
c = 1
t = n
print(' {} '.format(n), end='')
while c<10:
    t = t+r
    print(' -> {} '.format(t), end='')
    c+=1