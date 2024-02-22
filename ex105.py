def notas(*n,sit=False):
    """
    :param n: => Uma ou mais notas dos alunos
    :param sit: => opcção para adicionar situação
    :return: => dicionário para informar as situações da turma
    """
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média']>7:
            r['situação'] = 'BOA'
        elif 5< r['média']<=7:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r


resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)