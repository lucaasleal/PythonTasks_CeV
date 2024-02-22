num = ('zero', 'um', 'dois', 'três',
       'quatro', 'cinco', 'seis', 'sete',
       'oito' , 'nove', 'dez', 'onze',
       'doze', 'treze', 'quatorze', 'quinze',
       'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
resp = 'S'
while resp in 'SN':
    while True:
        n = int(input('Digite um número entre 0 e 20: '))
        if n>=0 and n<=20:
            break
        print('Tente novamente. ', end='')
    print(f'Voce digitou o número {num[n]}')
    resp = str(input('Quer continuar? [S/N]')).upper()
    if resp=='N':
        break
print('Fim do programa!')