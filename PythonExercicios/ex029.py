vel = float(input('Qual a velocidade atual do carro? '))
mul = (vel - 80)*7
if vel <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print(f'MULTADO! Você excedeu o limite permitido que é de 80Km/h\nVocê deve paar uma multa de R${mul:.2f}!')
    print('Tenha um bom dia! Dirija com segurança!')
