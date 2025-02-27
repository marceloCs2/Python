alt = float(input('Qual a sua altura(em metros): '))
peso = float(input('Qual o seu peso(em kg): '))
imc = peso/(alt**2)
print(f'Seu imc: {imc:.2f}')
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobre peso')
elif 30 <= imc < 40:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade mórbida')
