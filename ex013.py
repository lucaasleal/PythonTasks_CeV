print('Calculando Salário')
v = float(input('Valor do salário atual: R$'))
p = v + (v*0.15)
print('O valor do \033[1;36mnovo salário\033[m é igual a \033[1;32mR${:.2f}\033[m'.format(p))