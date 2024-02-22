from datetime import date
ano = date.today().year
maiores = 0
menores = 0
for c in range(1,8):
    nasc = int(input("Ano de Nascimento da {}° pessoa:".format(c)))
    idade = ano - nasc
    if idade>=21:
        maiores += 1
    else:
        menores += 1
print('Entre as 7 pessoas, {} são maiores \nE {} ainda não atingiram a maioridade'.format(maiores, menores))

