from random import shuffle

a = str(input(f'Diga um nome: '))
b = str(input(f'Fale outro nome: '))
c = str(input(f'Fale outro nome: '))
d = str(input(f'Fale só mais um nome: '))
lista = [a, b, c, d]
shuffle(lista)
print(f'a nova ordem é {lista}')