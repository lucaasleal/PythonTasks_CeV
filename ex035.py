print('-=-'*10)
print('IDEALIZADOR DE TRIÂNGULOS')
print('-=-'*10)
a = float(input('Primeiro Reta:'))
b = float(input('Segundo Reta:'))
c = float(input('Terceiro Reta:'))
if a+b>c and b+c>a and a+c>b:
    print('AS TRÊS RETAS FORMAM UM TRIÂNGULO!')
else:
    print('AS RETAS NÃO FORMAM UM TRIÂNGULO!')