sal = float(input('Qual é o salário do funcionário? R$'))
"""
if sal <= 1250:
    print(f'Seu salário era R${sal:.2f}, agora passou a ser R${sal + (sal * 0.15):.2f}')
else:
    print(f'Seu salário era R${sal:.2f}, agora passou a ser R${sal + (sal * 0.10):.2f}')
"""
if sal <= 1250:
    novo = sal + (sal*0.15)
else:
    novo = sal + (sal*0.10)
print(f'Seu salário era R${sal:.2f}, agora passou a ser R${novo:.2f}')
