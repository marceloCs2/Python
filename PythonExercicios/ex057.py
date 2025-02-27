sexo = str(input('Digite seu sexo [M/F]: '))
while sexo not in 'FfMm':
    sexo = str(input('Dado inválido. Digite novamente seu sexo [M/F]: '))
print('Dados cadastrados com sucesso')
