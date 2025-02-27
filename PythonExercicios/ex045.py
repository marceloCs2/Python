from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
print('Suas opções:\n[0] Pedra\n[1] Papel\n[2] Tesoura')
jogador = int(input('Qual é a sua jogada? '))
print('-='*11)
print(f'O computador jogou {itens[comp]}')
print(f'O jogador jogou {itens[jogador]}')
print('-='*11)

if comp == 0:
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('Jogador vence!')
    elif jogador == 2:
        print('Computador vence!')
    else:
        print('Jogada inválida!')
elif comp == 1:
    if jogador == 0:
        print('Computador vence!')
    elif jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('jogador vence!')
    else:
        print('Jogada inválida!')
elif comp == 2:
    if jogador == 0:
        print('Jogador vence!')
    elif jogador == 1:
        print('Computador vence!')
    elif jogador == 2:
        print('Empate"')
    else:
        print('Jogada inválida')