print('=====================')
print('CASA DE CÂMBIO')
print('=====================')
print('')
v = float(input('Digite o valor em reais: R$'))
d = v/4.93
e = v/5.36
l = v/6.27
print('O valor em doláres é igual a \033[1;32mUS${:.2f}\033[m'.format(d))
print('O valor em Euro é igual a \033[1;33m€{:.2f}\033[m'.format(e))
print('O valor em Libras é igual a \033[1;36m£{:.2f}\033[m'.format(l))