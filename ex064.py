tot = q = 0
n = 0
n=int(input('Digite o valor[999 para parar]:'))
while n!=999:
    tot = tot+n
    q += 1
    n = int(input('Digite o valor[999 para parar]:'))
print('A soma dos {} valores foi igual a {}'.format(q, tot))


