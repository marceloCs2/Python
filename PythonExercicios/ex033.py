pv = int(input('Digite o primeiro valor: '))
sv = int(input('Digite o segundo valor: '))
tv = int(input('Digite o terceiro valor:'))

menor = pv
if sv < pv and sv < tv:
    menor = sv
if tv < pv and tv < sv:
    menor = tv

maior = pv
if sv > pv and sv > tv:
    maior = sv
if tv > pv and tv > sv:
    maior = tv

print(f'O menor valor é: {menor}')
print(f'O maior valor é: {maior}')
