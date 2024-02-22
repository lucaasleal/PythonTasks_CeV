import datetime
nasc = int(input('Em que ano você nasceu?'))
sexo = str(input('Sexo:'))
ano = datetime.date.today().year
idade = ano - nasc
if sexo == 'Feminino':
    print('Seu sexo é feminino. Não há necessidade de alistamento!')
elif sexo == 'Masculino':
    if idade == 18:
     print('Você tem 18 anos! É hora de se ALISTAR!')
    elif idade<18:
        f = 18 - idade
        a = f + ano
        print('Você tem {} anos. Ainda faltam {} anos para se alistar.\nSeu alistamento será em {}'.format(idade, f, a))
    else:
        p = idade - 18
        ac = ano - p
        print('Voce já tem {} anos. Já se passaram {} anos do prazo correto.\nSeu alistamento foi em {}'.format(idade, p, ac))
