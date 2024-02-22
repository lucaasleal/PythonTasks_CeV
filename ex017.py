from math import hypot
print('CALCULADORA PITÁGORICA')
print('')
c1 = (float(input('Digite o valor do \033[34mprimeiro cateto\033[m: ')))
c2 = (float(input('Digite o valor do \033[35msegundo cateto\033[m: ')))
h = hypot(c1, c2)
print('O triângulo de catetos {} e {} tem hipotenusa de \033[1;36m{:.2f}'.format(c1, c2, h))