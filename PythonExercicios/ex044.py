pre = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[1] à vista dinheiro/cheque\n[2] à vista cartão\n[3]2x no cartão\n[4]3x ou mais no cartão')
opc = int(input('Qual é a opção? '))
if opc == 1:
    des = pre - (pre*0.10)
    print(f'Com o desconto, o valor passar a ser R${des:.2f}')
elif opc == 2:
    des = pre - (pre*0.05)
    print(f'Com o desconto, o valor passar a ser R${des:.2f}')
elif opc == 3:
    print(f'O preço continua R${pre:.2f}, com duas parcelas de R${pre/2:.2f}')
elif opc == 4:
    par = int(input('Quantas parcelas: '))
    juros = pre + (pre * 0.20)
    print(f'Com o juros, o preço final é de R${juros:.2f}.\nCom parcelas de R${juros/par}')
    