def metade(preço, format = False):
    '''
    Transformando na metade
    :param preço: valor inserido por o usuário
    :param format: Formatado ou não formatado
    :return: valor já trasnformado em metade
    '''
    valor = preço/2
    return valor if format is False else moeda(preço)



def dobro(preço = 0, format = False):
    valor = preço*2
    return valor if format is False else moeda(preço)


def aumentar(preço = 0,taxa=0, format=False):
    valor = preço*(1+(taxa/100))
    return valor if format is False else moeda(preço)


def diminuir(preço = 0,taxa=0, format=False):
    valor = preço*(1-(taxa/100))
    return valor if format is False else moeda(preço)

def moeda(preço = 0, moeda = "R$"):
    return f'{moeda}{preço:>.2f}'.replace('.',',')
