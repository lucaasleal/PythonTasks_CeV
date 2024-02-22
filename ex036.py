print('-=-=-MINHA CASA, MINHA VIDA-=-=-')
valor = float(input('Valor da casa: R$'))
sal = float(input('Valor do salário: R$'))
anos = int(input('Quantos anos de pagamento?'))
q = anos*12
p = valor / q
if p<=sal*0.3:
    print('Seu empréstimo está aprovado! Parcelas de R${:.2f} durante {} anos.'.format(p, anos))
else:
    print('Seu empréstimo foi negado! Para pagar R${:.2f} em {} anos a parcela é de R${:.2f}'.format(valor, anos, p))