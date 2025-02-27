sida = 0
mida = 0
maioridadehomem = 0
nomevelho = ''
mulh20 = 0
for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    ida = int(input('Idade: '))
    sex = str(input('Sexo [M/F]: ')).strip()
    sida += ida
    if p == 1 and sex in 'Mm':
        maioridadehomem = ida
        nomevelho = nome
    if sex in 'Mm' and ida > maioridadehomem:
        maioridadehomem = ida
        nomevelho = nome
    if sex in 'Ff' and ida < 20:
        mulh20 += 1
mida = sida / 4
print(f'A média de idade do grupo é de {mida} anos!')
print(f'O homem mais velho tem {maioridadehomem} e se chama {nomevelho}.')
print(f'Ao todos são {mulh20} mulheres com menos de 20 anos.')
