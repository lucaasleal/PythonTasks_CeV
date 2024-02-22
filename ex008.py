print('=========================')
print('CONVERSOR DE METROS')
print('=========================')
print('')
m = float(input('Valor em metros: '))
km = m / 1000
hm = m / 100
dam = m/10
dm = m * 10
cm = m * 100
mm = m * 1000
print('O valor de {} metros é igual a:'.format(m))
print(' \033[1;31m{}\033[m Quilômetros \n \033[1;32m{}\033[m Hectômetros \n \033[1;33m{}\033[m Decâmetros'.format(km, hm, dam))
print(' \033[1;34m{:.0f}\033[m Decímetros \n \033[1;35m{:.0f}\033[m Centímetros \n \033[1;36m{:.0f}\033[m Milímetros'.format(dm ,cm , mm) )
