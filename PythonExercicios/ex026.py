frase = str(input('Digite uma frase: ')).lower().strip()
vzs = frase.count('a')
pri = frase.find('a') + 1
ult = frase.rfind('a') + 1
print(f'A letra A aparece {vzs} vezes')
print(f'A primeira letra A apareceu na posição {pri}')
print(f'A última letra A apareceu na posição {ult}')
