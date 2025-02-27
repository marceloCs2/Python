print('='*20)
print('SUPER PA')
print('='*20)

pt = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
termo = pt
cont = 1
tot = 0
mais = 10
while mais != 0:
    tot += mais
    while cont <= tot:
        print(f'{termo} ->', end=' ')
        termo += raz
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')
