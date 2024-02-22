import random
from time import sleep
print('-----ADIVINHE O NÚMERO-----')
n = random.randint(1,5)
print('-=-'*20)
nu = int(input('Adivinhe o número que escolhi(1 a 5):'))
print('-=-'*20)
print('PROCESSANDO...')
sleep(3)
if nu == n:
  print('PARABÉNS, VOCÊ VENCEU!')
else:
    print('QUE PENA, VOCÊ PERDEU! Pensei no {}'.format(n))
print('Obrigado Por Jogar!')
