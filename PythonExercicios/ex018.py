from math import sin, cos, tan, radians

num = int(input('Digite o ângulo que desejar(inteiro): '))
sen = sin(radians(num))
cose = cos(radians(num))
tang = tan(radians(num))
print(f'Os valores de seno, cosseno e tangente do angulo {num} são respectivamente:\n{sen:.2f},{cose:.2f},{tang:.2f}')
