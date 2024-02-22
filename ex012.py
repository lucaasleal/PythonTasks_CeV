print('CALCULADOR DE DESCONTOS')
p = float(input('Valor do produto: '))
v = p - (p*0.05)
print('O valor do produto com \033[31m5% de desconto\033[m é de \033[32mR${:.2f}\033[m'.format(v))