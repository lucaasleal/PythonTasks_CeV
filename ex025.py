nome = str(input('Qual é o seu nome completo?')).strip()
n = 'silva' in nome.lower()
if n == True:
    print('\033[32mSeu nome tem silva!\033[m')
else:
    print('\033[31mSeu nome não tem silva!\033[m')

