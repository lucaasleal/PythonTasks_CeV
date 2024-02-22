aluno = {}
aluno['Nome'] = str(input('Nome:'))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}:'))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno["média"] <7:
    aluno['Situação'] = 'em Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
print('-=-'*10)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')