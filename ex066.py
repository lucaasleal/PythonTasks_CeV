n = cont = s = 0
while True:
    n = int(input('Digite um número [999 p/ Parar]: '))
    if n == 999:
        break
    cont += 1
    s+=n
print(f'A soma dos {cont} valores foi igual a {s}!')