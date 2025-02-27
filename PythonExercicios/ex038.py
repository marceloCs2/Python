num = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
if num > num2:
    print(f'O primeiro valor é maior.')
elif num2 > num:
    print(f'O segundo valor é maior.')
elif num == num2:
    print(f'Não existe valor maior, os dois são iguais.')
