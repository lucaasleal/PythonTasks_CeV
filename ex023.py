num = int(input('Digite um número de até 4 dígitos: '))
u = num//1 % 10
d = num//10 % 10
c = num//100 % 10
m = num//1000 % 10
print('Unidade: \033[36m{}\033[m'.format(u))
print('Dezena: \033[34m{}\033[m'.format(d))
print('Centena: \033[35m{}\033[m'.format(c))
print('Milhar: \033[31m{}\033[m'.format(m))