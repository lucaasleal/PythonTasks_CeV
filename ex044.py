print('-=-=-LOJA GUANABARA-=-=-')
valor = float(input('Valor do produto:'))
print('''Forma de pagamento:
[1] À vista no dinheiro/cheque
[2] À vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
r = int(input('Qual é a opção?'))
if r==1:
  p = valor*0.9
  print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, p))
if r==2:
  p = valor*0.95
  print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, p))
if r==3:
   print('O valor final é de R${:.2f}'.format(valor))
if r==4:
   n = int(input('Número de parcelas:'))
   p = valor*1.2
   parcela = p/n
   print('Sua compra de R${:.2f} vai custar R${:.2f} no final.\nSua compra será parcelada em {}x de R${:.2f} sem juros'.format(valor, p, n, parcela))
else:
    print('\033[31mOPÇÃO INVÁLIDA! Tente novamente.\033[m')