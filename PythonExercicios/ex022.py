nome = str(input('Digite seu nome completo: ')).strip()
mai = nome.upper()
miu = nome.lower()
com = len(nome) - nome.count(' ')
separa = nome.split()
print(f'Analisando seu nome...\nEm maiúsculo é {mai}\nEm minúscula é {miu}')
print(f'Seu nome tem ao todo {com} letras')
print(f'Seu primeiro nome é {separa[0]} e ele tem o todo {len(separa[0])} letras')
