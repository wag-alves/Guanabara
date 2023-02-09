
x = int(input(f'Qual a velocidade que você estava? '))

if x > 80:
    print(f'Sua velocidade é {x} e você terá que pagar uma multa de {(x - 80) * 7}')

else:
    print(f'Você é um exemplo de cidadão, sua velocidade foi {x}')