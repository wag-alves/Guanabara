algo = input(f'Digite algo:')
print(f'O tipo primitivo desse valor é {type(algo)}')
print(f'Só tem espaços?{algo.isspace()}')
print(f'É um número?{algo.isnumeric()}')
print(f'É alfabetico?{algo.isalpha()}')
print(f'É alfanumérico?{algo.isalnum()}')
print(f'Está em maiúscula?{algo.isupper()}')
print(f'Está em minúscula?{algo.islower()}')
print(f'Está capitalizado?{algo.istitle()}')