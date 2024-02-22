print('SEQUÊNCIA DE FIBONACCI')
print('-=-'*10)
n = int(input('Digite o números de termos:'))
num1 = num2 = 1
f = 0
c = 0
print('~'*20)
print('{} -> {}'.format(f , num1), end='')
while c!=(n-2):
    print(' -> {} '.format(num2), end='')
    f = num1
    num1 = num2
    num2 = f + num1
    c+=1
print('FIM')
