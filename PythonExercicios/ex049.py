num = int(input('Digite um número para ver a tabuada: '))
for c in range(0, 11):
    mul = c*num
    print(f'{num} x {c} = {mul}')
print(f'Essa é a tabuada do {num}!')