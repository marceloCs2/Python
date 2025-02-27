casa = float(input('Valor da casa: R$'))
sal = float(input('Salário do comprador: R$'))
anos = float(input('Quantos anos de financiamento? '))
pre = casa/(anos*12)
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos a prestação será de R${pre:.2f}.')
if pre > sal*0.3:
    print(f'Empréstimo NEGADO')
else:
    print(f'Empréstimo PERMITIDO')
