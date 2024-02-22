import datetime
nasc = int(input('Ano de Nascimento:'))
ano = datetime.date.today().year
idade = ano - nasc
print('O atleta tem {} e faz parte da categoria:'.format(idade))
if idade<=9:
    print('MIRIM')
elif idade<=14:
    print('INFANTIL')
elif idade<=19:
    print('JÚNIOR')
elif idade==20:
    print('SÊNIOR')
else:
    print('MASTER')