a = float(input('Primeiro lado:'))
b = float(input('Segundo lado:'))
c = float(input('Terceiro lado:'))
if a+b>c and b+a>c and  b+c>a:
  print('Com lados {}, {} e {} é possível formar um triângulo!'.format(a, b, c))
  if a==b and b==c:
    print('O triângulo é EQUILÁTERO!')
  elif a != b != c != a:
    print('O triângulo é ESCALENO!')
  else:
      print('O triângulo é ISÓSCELES!')
else:
    print('É impossível formar um triângulo!')