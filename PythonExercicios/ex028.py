from random import randint
comp = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 a 5. Tente adivinhar...')
print('-=-' * 20)
jog = int(input('Em que número eu pensei? '))
if jog == comp:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {comp} e não no {jog}!')
