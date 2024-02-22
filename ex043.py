print('CALCULADORA DE IMC')
p = float(input('Digite seu peso(Kg):'))
a = float(input('Digite sua altura(m):'))
imc = p/(a**2)
print('Seu IMC é de {:.2f}'.format(imc))
if imc<=18.5:
    print('Você está ABAIXO do peso!')
elif imc<=25:
    print('Você está no peso IDEAL!')
elif imc<=30:
    print('Você está SOBREPESO!')
elif imc<=40:
    print('Você está em OBESIDADE, cuidado!')
else:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')

