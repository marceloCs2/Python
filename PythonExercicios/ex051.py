print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)

pt = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
dec = pt + (10-1) * raz
for c in range(pt, (dec + raz), raz):
    print(f'{c}')
print('Acabou')

