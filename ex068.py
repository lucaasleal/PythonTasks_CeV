from random import randint
n = c = s = v = 0
pi = ''
print('-=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=-'*15)
while True:
    n = int(input('Diga um valor: '))
    c = randint(1,10)
    pi = str(input('Par ou Ímpar? [P/I] ')).upper()
    s = n + c
    if s%2==0 and pi=='P':
        print('-'*45)
        print(f'Você jogou {n} e o computador jogou {c}. Total de {s} deu PAR')
        v+=1
    elif s%2==1 and pi=='I':
        print('-'*45)
        print(f'Você jogou {n} e o computador jogou {c}. Total de {s} deu ÍMPAR')
        v += 1
    elif s%2==1 and pi=='P':
        print('-' * 45)
        print(f'Você jogou {n} e o computador jogou {c}. Total de {s} deu ÍMPAR')
        break
    elif s%2==0 and pi=='I':
        print('-' * 45)
        print(f'Você jogou {n} e o computador jogou {c}. Total de {s} deu PAR')
        break
    print('-' * 45)
    print('VOCÊ VENCEU!')
    print('Vamos jogar novamente...')
print('VOCÊ PERDEU!')
print('-=-'*15)
print(f'GAME OVER! Você venceu {v} vezes.')