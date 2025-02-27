print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)

pt = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
cont = 1
while cont <= 10:
    print(f'{pt}')
    pt += raz
    cont += 1
print('FIM')
