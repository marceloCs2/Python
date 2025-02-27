"""
preco = float(input('Qual o preço do produto? R$'))
promo = preco*0.05
des = (preco-promo)
print(f'O produto custa R${preco}, porém com um desconto de 5% passa a ser R${des}')
"""

preco = float(input('Qual o preço do produto? R$'))
novo = preco - (preco*0.05)
print(f'O produto custa R${preco}, porém com um desconto de 5% passa a ser R${novo}')
