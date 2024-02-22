from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
c = randint(0,2)
print('''Escolha sua opção:
[0] Pedra
[1] Papel
[2] Tesoura''')
j = int(input("Qual sua jogada?"))
print('-=-'*10)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('Computador jogou {}'.format(itens[c]))
print('Jogador jogou {}'.format(itens[j]))
print('-=-'*10)
if j==0 and c==2 or j==1 and c==0 or j==2 and c==1:
    print('JOGADOR VENCE!')
elif j==c:
    print('EMPATE')
else:
    print('COMPUTADOR VENCE!')