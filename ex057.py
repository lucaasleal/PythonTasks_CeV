sexo = str(input('Informe seu sexo [M/F]:')).strip().upper()[0]
while sexo not in "MmFf":
    sexo = str(input('Dados Inválidos! Digite seu sexo [M/F]:')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))