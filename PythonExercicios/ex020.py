from random import shuffle

al1 = str(input('Primeiro aluno: '))
al2 = str(input('Segundo aluno: '))
al3 = str(input('Terceiro aluno: '))
al4 = str(input('Quarto aluno: '))

lista = [al1, al2, al3, al4]
shuffle(lista)
print('*'*15)
print(f'A ordem de apresentação será\n{lista}')
print('*'*15)
