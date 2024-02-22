from time import sleep
def contagem(a, b, c):
    if c == 0:
        c = 1
    if c < 0:
        c *= -1
    print('-=-'*10)
    print(f'Contagem de {a} até {b} de {c} em {c}')
    sleep(2)
    if b>=a:
       num = a
       while num<=b:
            print(f"{num} ", end ='', flush=True)
            sleep(0.3)
            num += c
       print('FIM!')
    else:
        num = a
        while num>=b:
            print(f"{num} ", end='', flush=True)
            sleep(0.3)
            num-=c
        print('FIM!')
contagem(1, 10, 1)
contagem(10, 0, 2)
print('-=-'*10)
print('Agora é sua vez de personalizar sua contagem!')
a = (int(input('Início: ')))
b = (int(input('Fim: ')))
c = int(input('Passo: '))
contagem(a, b, c)
