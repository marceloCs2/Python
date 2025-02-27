from datetime import date
ano = date.today().year
nas = int(input('Ano de nascimento: '))
ida = ano - nas
print(f'O atleta tem {ida} anos, ele é: ')
if ida <= 9:
    print('MIRIM')
elif ida <= 14:
    print('INFANTIL')
elif ida <= 19:
    print('JÚNIOR')
elif ida <= 25:
    print('SÊNIOR')
elif ida > 25:
    print('MASTER')
    