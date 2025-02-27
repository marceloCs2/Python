from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opc = 0
while opc != 5:
    print('[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos números\n[5]sair do programa')
    opc = int(input('Qual é a sua opção: '))
    if opc == 1:
        print(f'{n1} + {n2} = {n1+n2}')
    elif opc == 2:
        print(f'{n1} x {n2} = {n1*n2}')
    elif opc == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}, logo o primeiro valor é maior.')
        elif n1 == n2:
            print(f'Os valores são iguais.')
        else:
            print(f'{n2} é maior que {n1}, logo o segundo valor é maior.')
    elif opc == 4:
        print('Escolha novos números!')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    else:
        print('Fim')
    sleep(1.5)
print('Você saiu do programa.')