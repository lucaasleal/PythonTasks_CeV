nome = str(input('Digite seu nome completo: ')).strip().split()
print('Primeiro nome: {}'.format(nome[0]))
print('Último nome: {}'.format(nome[len(nome)-1]))