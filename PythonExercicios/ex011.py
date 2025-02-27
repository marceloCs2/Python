largura = float(input('Qual a largura da parede?: '))
altura = float(input('Qual a altura da parede?'))
area = (largura*altura)
tinta = area/2
print(f'A dimensão da sua parede é de {largura}x{altura}\nSua área é de {area}m2')
print(f'Para pintar essa parede, é necessário {tinta:.2f}l de tinta')
