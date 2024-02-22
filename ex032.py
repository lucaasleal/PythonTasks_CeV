from datetime import date
print('===ANO BISSEXTO===')
a = int(input('Digite o ano:'))
r = a%4
if a == 0:
    a = date.today().year
if r==0 and a%100 != 0 or a % 400 ==0:
    print('O ANO DE {} É BISSEXTO!'.format(a))
else:
    print('O ANO DE {} NÃO É BISSEXTO!'.format(a))