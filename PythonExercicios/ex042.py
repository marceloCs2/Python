
num = float(input('Primeiro segmento: '))
num2 = float(input('Segundo segmento: '))
num3 = float(input('Terceiro segmento: '))

if num < num2 + num3 and num2 < num + num3 and num3 < num + num2:
    print(f'Esses segmentos podem sim, formar um triângulo. ')
    if num == num2 == num3:
        print('Equilátero')
    elif num != num2 != num3 != num:
        print('Escaleno')
    else:
        print('Isósceles')

else:
    print(f'Esses segmentos não podem formar um triângulo')
