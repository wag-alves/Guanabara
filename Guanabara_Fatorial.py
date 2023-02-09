

n = int(input(f'Digite um número: '))
contador = n
if n == 0 or n == 1:
    print(f'Fatorial igual a 1.')
    while contador > 1:
        x = n - 1
        contador = contador - 1
print(n, contador)
