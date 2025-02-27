dis = float(input('Qual a distância da sua viagem (Km): '))
d50 = (dis * 0.5)
d45 = (dis * 0.45)
print(f'Você esta prestes a começar uma viagem de {dis}Km.')
if dis <= 200:
    print(f'O preço da sua passagem é R${d50:.2f}')
else:
    print(f'O preço da sua passagem é R${d45:.2f}')
