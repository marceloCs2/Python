from datetime import date
ano = date.today().year
nas = int(input('Ano do seu nascimento: '))
ida = ano - nas
print(f'Quem nasceu em {nas} tem {ida} anos em {ano}.  ')
if ida < 18:
    print(f'Ainda faltam {18 - ida} anos para o alistamento')
    print(f'Seu alistamento srá em {(18 - ida) + ano}.')
elif ida > 18:
    print(f'Já se passaram {ida - 18} anos do seu alistamento')
    print(f'Seu alistamento foi em {ano - (ida - 18)}')
elif ida == 18:
    print(f'Você deve se alistar imediatamente')
