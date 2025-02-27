try:
    nome = str(input('Digite seu nome completo: ')).strip()
    n = nome.split()
    print(f'Seja bem vindo {nome}!')
    print(f'Seu primeiro nome é {n[0]}')
    print(f'Seu último nome é {n[-1]}')
except Exception as ERRO:
    print(f'ERRO: {ERRO}')