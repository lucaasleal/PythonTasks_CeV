def fatorial(n=0, show=False):
    """
    :param n: O número a ser calculado
    :param show: Opcão para mostrar ou não a conta
    :return: O valor do fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show == True:
            print(c, end='')
            if c>1:
              print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(10, show = True))