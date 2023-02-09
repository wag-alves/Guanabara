
'''
c = 1

while c < 10:
    print(c)
    c = c + 1
print(f'Você é incrivel!!')

'''
'''
r = 's' 

while r == 's':
    x = int(input(f'Digite um valor: '))
    r = str(input(f'Você quer continuar?'))
print(f'Fim')

'''
'''
x = 1
par = impar = 0

while x != 0:
    x = int(input(f'Digite um valor: '))
    if x != 0:
        if x % 2 == 0:
            par = par + 1
        else:
            impar = impar +  1
print(f'Há {par} números pares e {impar} números ímpares')

'''

'''
sexo = str(input(f'Digite o seu sexo.'))
while sexo != 'm' or sexo != 'f':
    print(f'Sexo inválido') # loop infinito de sexo inválido
print(sexo)
'''

#esta questao esta errada
'''
sexo = str(input(f'Digite o seu sexo: '))
while sexo == 'h' or sexo == 'm':
    sexo = str(input(f'Dados inválidos, digite de novo.'))
print(sexo)
'''
'''

from random import randint
computador = randint(0, 10)
print(f'Sou seu computador... Estou pensando em um número entre 0 e 10...')
print(f'Será que você consegue adivinhar qual foi? ')
acertou = False
palpite = 0

while not acertou:
    jogador = int(input(f'Qual é o seu palpite? '))
    palpite = palpite + 1
        #Se a pessoa acertou de primeira ele vai parar o jogo...
    if jogador == computador:
        acertou = True
    
    else:
        if jogador < computador:
            print(f'Mais... Tente de novo.')
        elif jogador > computador:
            print(f'Menos... Tente de novo.')
print(f'Você acertou com {palpite} palpites!!')


'''



from time import sleep
n1 = int(input(f'Digite um número '))
n2 = int(input(f'Digite outro número '))
opção = 0
while opção != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opção = int(input(f'Qual é a sua opção?'))
    if opção == 1:
        soma = n1 + n2
        print(f'A soma de {n1} + {n2} é {soma}')
    elif opção == 2:
        mult = n1 * n2
        print(f'A multiplicação de {n1} x {n2} é {mult}')
    elif opção == 3:
        if n1 > n2:
            print(f'O maior é {n1}')
        else:
            print(f'O maior é {n2}')
    elif opção == 4:
        print(f'Informe os números novamente: ')
        n1 = int(input(f'Digite o primeiro valor: '))
        n2 = int(input(f'Digite o segundo valor: '))
    elif opção == 5:
        print(f'Finalizando o programa.')
    else:
        print(f'Valor inválido, tente novamente.')
    print('=-=' * 10)
    sleep(1)
sleep(2)
print(f'Fim do programa! Volte de sempre!')

