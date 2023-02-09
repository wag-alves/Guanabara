from random import choice

lista = [0, 1, 2, 3, 4, 5]
y = choice(lista)

x = int(input(f'Estou pensando em um número entre 0 e 5, adivinhe qual é: '))

if x == y:
    print(f'Você acertou, Parabéns!!! Eu pensei em {y} e você em {x}. Bem que eu sabia que gênios pensam iguais...')

else:
    print(f'Você falou {x} e eu pensei em {y}, mais sorte na próxima vez.')    