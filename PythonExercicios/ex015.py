dia = int(input('Quantos dias o carro ficou alugado?: '))
km = float(input('Quantos Km o carro rodou?:'))
pdi = 60*dia
pkm = 0.15*km
tot = pdi+pkm
print(f'O valor pelo dia foi de R${pdi}.\nO valor por km rodado foi de R${pkm}')
print(f'O valor total a ser pago é: R${tot}')