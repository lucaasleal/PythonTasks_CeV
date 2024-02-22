si = 0
media = 0
maioridade = 0
nomevelho = ''
mnovas = 0
for c in range(1,5):
   print('----{}ºPESSOA----'.format(c))
   n = str(input('Nome:'))
   i = int(input('Idade:'))
   s = str(input('Sexo[M/F]:'))
   si += i
   if c==1 and s in 'Mm':
      maioridade = i
      homemvelho = n
   if s in "Mm" and i>maioridade:
      maioridade = i
      homemvelho = n
   if s in 'Ff' and i<20:
      mnovas += 1
media = si/4
print('A média da idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e seu nome é {}'.format(maioridade, homemvelho))
print('Há {} mulheres com menos de 20 anos'.format(mnovas))
