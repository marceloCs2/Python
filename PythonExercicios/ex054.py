from datetime import date
ano = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    nas = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    if ano - nas >= 18:
        maior += 1
    else:
        menor += 1
print(f'Ao todo tivemos {maior} pessoas maiores de idade')
print(f'Ao todo tivemos {menor} pessoas menores de idade')
