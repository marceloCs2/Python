num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para a conversão:\n[1]BINÁRIO\n[2]OCTAL\n[3]HEXADECIMAL')
opc = int(input('Sua opção: '))
if opc == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}.')
elif opc == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}.')
elif opc == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}.')
else:
    print('\033[1;30;41m[ERRO]AS OPÇÕES DEVEM SER DE 1 A 3[ERRO]\033[m')
