print('===É PAR ou ÍMPAR?===')
n = int(input('Digite o número:'))
r = n % 2
if r==0:
   print('O NÚMERO {} É PAR!'.format(n))
else:
    print('O NÚMERO {} É ÍMPAR!'.format(n))