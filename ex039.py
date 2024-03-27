from time import sleep
print('VAMOS CALCULAR SEU IMC, É MUITO IMPORTANTE')
print(f'-=-=' * 20)
peso = float(input('DIGITE SEU PESO:'))
altura = float(input('DIGITE SUA ALTURA:'))
print(f'-=-=' * 20)
imc = peso/((altura*altura))
print('calculando...')
sleep(3)
print(f'-=-=' * 20)

if imc < 18.5:
    print(f'ABAIXO DO PESO, IMC = {imc} !')
elif imc >= 18.5 and imc <= 25:
    print(f'PESO IDEAL, IMC = {imc}')
elif 25 > imc <= 30:
    print(f'SOBREPESO, IMC = {imc}')
elif 30 > imc <= 40:
    print(f'OBESIDADE, IMC = {imc}')
else:
    print(f'OBESIDADE MÓRBIDA, IMC = {imc}')

print(f'-=-=' * 20)