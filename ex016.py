import math
n = float(input('Digite um número: '))
i = math.trunc(n)
print('O número \033[33m{}\033[m tem parte inteira \033[1;35m{}'.format(n, i))