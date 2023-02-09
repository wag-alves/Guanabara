import math

angulo = float(input(f'Digite o ângulo que você deseja: '))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tg = math.tan(math.radians(angulo))
print(f'O angulo {angulo} tem COS = {cos:.2f} SEN = {sen:.2f} e TG = {tg:.2f}')
