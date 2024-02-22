s = 0
p = 0
for c in range(1, 7):
    n = int(input('Digite um número:'))
    if n%2==0:
        s += n
        p += 1
print('A soma de todos os {} números PARES é igual a {}'.format(p, s))