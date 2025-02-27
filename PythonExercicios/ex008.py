medida = float(input('Uma distância em metros: '))
km = medida*0.001
hm = medida*0.01
dam = medida*0.1
dm = medida*10
cm = medida*100
mm = medida*1000
print(f'A medida de {medida}m corresponde a:\n{km}km\n{hm}hm\n{dam:.1f}dam\n{dm}dm\n{cm}cm\n{mm}mm')
