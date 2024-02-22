n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1+n2)/2
if m<5:
    print('Média igual a {:.1f}. Você está REPROVADO!'.format(m))
elif m>=7:
    print('Média igual a {:.1f}. Você está APROVADO!'.format(m))
else:
    print('Média igual a {:.1f}. Você está em RECUPERAÇÃO!'.format(m))
