num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        tot += 1
    print(c, end='   ')
print(f'\n\033[mO número {num} foi divisível {tot} vezes')
if tot == 2:
    print('Ele é primo!')
else:
    print('Ele não é primo!')
