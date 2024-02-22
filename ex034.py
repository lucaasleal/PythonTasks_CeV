print('-=-=-=-AUMENTO SALARIAL-=-=-=-')
s = int(input('Digite o salário atual:'))
if s<=1250:
    novo=s*1.15
else:
    novo=s*1.1
print('Seu novo salário é de R${:.2f}'.format(novo))
