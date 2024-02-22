from time import sleep
n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
r = s = m = 0
while r != 5:
    print('-=-'*20)
    print('''Selecione uma opção:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    r = int(input('Qual sua opção? '))
    if r==1:
        s = n1 + n2
        print('A soma entre {} e {} é igual a {}.'.format(n1, n2, s))
    if r==2:
        m = n1 * n2
        print('O produto entre {} e {} é igual a {}'.format(n1 , n2, m))
    if r==3:
        if n1>n2:
            print('O maior número é {}'.format(n1))
        else:
            print('O maior número é {}'.format(n2))
    if r==4:
        n1 = int(input('Digite o 1° número: '))
        n2 = int(input('Digite o 2° número: '))
    if r>5:
        print('Opção Inválida. Tente Novamente')
print('Finalizando...')
sleep(1)
print('-=-'*20)
print('Você saiu do programa!')
