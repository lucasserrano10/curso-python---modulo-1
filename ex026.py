velocidadeCarro = float(input('QUAL ERA A VELOCIDADE DO SEU CARRO NA VIA :'))
if velocidadeCarro > 70:
    multa = (velocidadeCarro - 70) * 7
    print(f'MULTADO ! VALOR : {multa}')
else :
    print('NÃO FOI MULTADO, SEM MULTA !')