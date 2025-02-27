nt1 = float(input('Primeira nota: '))
nt2 = float(input('Segunda nota: '))
med = (nt1 + nt2) / 2
print(f'Sua média foi {med:.2f}.')
if med < 5:
    print('REPROVADO!')
elif med <= 6.9:
    print('RECUPERAÇÃO!')
elif med >= 7:
    print('APROVADO! Boas férias!')
