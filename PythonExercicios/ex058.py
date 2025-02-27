from random import randint
comp = randint(0, 10)
print('O computador escolheu um número de 0 a 10')
acertou = False
palp = 0
while not acertou:
    jog = int(input('Qual é o seu palpite: '))
    palp += 1
    if jog == comp:
        acertou = True
    else:
        if jog < comp:
            print('Errou! tente um valor mais alto')
        else:
            print('Errou! tente um valor mais baixo ')
print(f'Acertou com {palp} tentativas.')