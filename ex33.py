print('ÁREA DE EMPRÉSTIMOS !')

print(f'-=-='*20)

casaValor = float(input('VALOR DA CASA :'))
salarioCliente = float(input("SALÁRIO DO COMPRADOR :"))
anos = int(input('QUANTOS ANOS VOCÊ GOSTARIA DE FAZER AS PARCELAS ?'))

prestacao = (casaValor/anos)/12

if salarioCliente <= (0.7 * prestacao):
    print('EMPRÉSTIMO NEGADO')
else:
    print('FINANCIAMENTO APROVADO !')