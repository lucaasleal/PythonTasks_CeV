nh = nm = pi = 0
idade = 0
while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)
    idade = int(input('Idade:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).upper()
    if idade>17:
        pi+=1
    if idade<20 and sexo=='F':
        nm+=1
    if sexo=='M':
        nh+=1
    r = ' '
    while r not in 'SN':
     r = str(input('Quer continuar? [S/N]')).upper()
    if r=="N":
       break
print('=====FIM DO PROGRAMA=====')
print(f'Total de pessoas com mais de 18 anos: {pi}')
print(f'Ao todo temos {nh} homens cadastrados')
print(f"E temos {nm} mulheres com menos de 20 anos")

