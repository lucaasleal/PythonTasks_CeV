from random import randint
lista = []
print('-'*30)
print('JOGUE NA MEGA SENA'.center(30))
print('-'*30)
num = int(input('Quantos jogos você quer que eu sorteie? '))
print(F'-=-=-=  SORTEANDO {num} JOGOS  -=-=-=')
for c in range(1, num+1):
    for l in range (1,7):
        lista.append(randint(0,60))
    lista.sort()
    print(f'Jogo {c}: {lista}')
    lista.clear()
print('-=-=-=-=-= < BOA SORTE! > -=-=-=-=-=')

