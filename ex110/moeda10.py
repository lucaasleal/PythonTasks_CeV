def metade(preço, format = False):
    valor = preço/2
    return valor if format is False else moeda(valor)


def dobro(preço = 0, format = False):
    valor = preço*2
    return valor if format is False else moeda(valor)


def aumentar(preço = 0,taxa=0, format=False):
    valor = preço*(1+(taxa/100))
    return valor if format is False else moeda(valor)


def diminuir(preço = 0,taxa=0, format=False):
    valor = preço*(1-(taxa/100))
    return valor if format is False else moeda(valor)

def moeda(preço = 0, moeda = "R$"):
    return f'{moeda}{preço:>.2f}'.replace('.',',')


def resumo(preço=0, a=0,r=0):
    print('-'*30)
    print('       RESUMO DO VALOR')
    print('-'*30)
    print(f'Preço Analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço,True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{a}% de Aumento: \t{aumentar(preço, a, True)}')
    print(f'{r}% de Redução: \t{diminuir(preço, r, True)}')
    print('-'*30)