produto = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2,
           'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)
print('---'*13)
print(f'{"LISTAGEM DE PREÇOS":^39}')
print('---'*13)
for pos in range(0, len(produto)):
    if pos%2==0:
     print(f'{produto[pos]:.<30}', end='')
    if pos%2==1:
     print(f'R${produto[pos]:>7.2f}')
print('---'*13)
