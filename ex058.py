from random import randint
print('Acabei de pensar em um número entre 0 e 10!')
c = randint(0,11)
v = 0
n = int(input('Adivinhe o número:'))
while c!=n:
    if c>n:
        print('Mais...', end=' ')
    else:
        print('Menos...', end=' ')
    n = int(input('Incorreto. Tente adivinhar novamente: '))
    v+=1
print('VOCÊ VENCEU! Mas foram necessários {} palpites'.format(v))