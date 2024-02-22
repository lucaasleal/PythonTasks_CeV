print('CONVERSOR DE TEMPERATURAS')
t = float(input('Digite a temperatura em Celsius: '))
f = ((9*t)/5) + 32
print('O valor de \033[33m{}°C\033[m em Fahrenheit é igual a \033[34m{}°F\033[m!'.format(t, f))