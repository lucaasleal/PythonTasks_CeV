print('CALCULANDO TINTA')
c = float(input('Comprimento da parede: '))
a = float(input('Altura da parede: '))
p = c*a
l = p/2
print("Para pintar uma parede de {} m² é necessario \033[1:46m{}\033[m litros de tinta".format(p, l))