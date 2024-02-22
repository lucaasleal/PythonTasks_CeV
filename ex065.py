n = int(input('Digite um valor: '))
media = 0
cont = 1
maior = menor = soma = n
c = str(input('Quer continuar?[S/N] ')).upper()
while c=='S':
    n = int(input('Digite um valor: '))
    soma += n
    cont += 1
    if n>=maior:
        maior = n
    if n<=menor:
        menor = n
    c = str(input('Quer continuar?[S/N] ')).upper()
media = soma/cont
print('A média entre os {} valores é igual a {}.'.format(cont, media))
print('O maior número foi {} e o menor foi {}.'.format(maior , menor ))
