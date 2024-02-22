print('============================')
print('\033[1;31mCALCULADORA ESCOLAR\033[m')
print('============================')
print("")
nome = input('\033[4;37mAluno:\033[m')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print("A média de \033[4;32m{}\033[m foi \033[1:35m{:.1f}".format(nome, m))