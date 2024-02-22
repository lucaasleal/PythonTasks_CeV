print('-=-=-=-=-=-RADAR DE VELOCIDADE-=-=-=-=-=-')
v = int(input('Qual é a velocidade do carro? '))
if v > 80:
    p = (v-80)*7
    print('MULTADO! Excedeu o limite de 80km/h \n Valor da multa: R${:.2f}'.format(p))
else:
    print('Velocidade Segura! Siga viagem.')