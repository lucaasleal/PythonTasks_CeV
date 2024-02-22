n1 = int(input('\033[35mDigite um valor: '))
n2 = int(input('\033[33mDigite outro valor:\033[m '))
s = n1 + n2
print('A soma entre \033[32m{}\033[m e \033[31m{}\033[m é igual a \033[36m{}'.format(n1,n2,s))
