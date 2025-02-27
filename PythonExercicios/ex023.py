num = int(input('Informe um número (0-9999) : '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando seu número...\nUnidade:{u}\nDezena:{d}\nCentena:{c}\nMilhar{m}')
