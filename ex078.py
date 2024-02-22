lista = []
maior = 0
menor = 0
for c in range(0,5):
    lista.append(int(input(f'Digite o valor da posição {c}:')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c]>maior:
            maior = lista[c]
        if lista[c]<menor:
            menor = lista[c]
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} nas posições ', end = '')
for i, v in enumerate(lista):
    if v == maior:
        print(f' {i}... ', end = '')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f" {i}... ", end='')
print()