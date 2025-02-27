try:
    from math import hypot

    co = float(input('Comprimento do cateto oposto: '))
    ca = float(input('Comprimento do cateto adjacente: '))
    hi = hypot(co, ca)

    print(f'A hipotenusa mede {hi:.2f}')
except:
    print('Erro')
