from datetime import date
pessoa = {}
pessoa['Nome'] = str(input('Nome: '))
pessoa['Idade'] = date.today().year - int(input('Ano de nascimento: '))
pessoa['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['CTPS'] > 0:
    pessoa['Contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário: R$'))
    pessoa['Aposentadoria'] = 35 + pessoa['Contratação'] - (date.today().year - pessoa['Idade'])
for k,v in pessoa.items():
    print(f'{k} tem o valor {v}.')

