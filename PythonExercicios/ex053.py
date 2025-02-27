frase = str(input('Digite uma frase: ')).strip().upper()
pal = frase.split()
junto = ''.join(pal)
inv = junto[::-1]
print(junto, inv)
if inv == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')