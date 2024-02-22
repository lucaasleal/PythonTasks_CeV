from datetime import date
def voto(ano):
    idade = date.today().year - ano
    if idade<16:
        return(f'Com {idade} anos: NÃO VOTA.')
    elif idade>=65 or 16 <= idade <18:
        return(f'Com {idade} anos: VOTO OPCIONAL.')
    else:
        return(f'Com {idade} anos: VOTO OBRIGATÓRIO.')


nasc = voto(int(input('Em que ano você nasceu? ')))
print(nasc)