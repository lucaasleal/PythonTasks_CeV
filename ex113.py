def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido!\033[m')
        except KeyboardInterrupt:
            print('\033[36mEntrada de dados interrompida pelo Usuário.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except KeyboardInterrupt:
            print('\033[36mEntrada de dados interrompida pelo Usuário.\033[m')
            return 0
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido!\033[m')
        else:
            return n


num = leiaInt('Digite um inteiro: ')
real = leiaFloat('Digite um real: ')
print(f'O valor inteiro foi {num} e o valor real foi {real}')