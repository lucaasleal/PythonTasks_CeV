n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} é \033[33m{}\033[m, seu triplo é \033[35m{}\033[m e sua raiz quadrada é \033[36m{:.2f}\033[m!'.format(n, d, t, r))
