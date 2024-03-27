print('ÁREA DE COMPRA !')
precoProduto = float(input('PREÇO DO PRODUTO :'))
formaPagamento = int(input('FORMA DE PAGAMENTO, 1-DINHEIRO, 2-DÉBITO, 3-1X OU 2X CARTÃO,4-MAIS DE 3X CARTÃO :'))
print(f'-=-=' * 20)

if formaPagamento == 1:
    print('FORMA DE PAGAMENTO : DINHEIRO')
    conta = (precoProduto*0.9)
    desconto = conta - precoProduto
    print(f'COM 10% DE DESCONTO, TOTAL : {conta}')
    print(f'VALOR DO DESCONTO : {desconto}')
elif formaPagamento == 2:
    print('FORMA DE PAGAMENTO : DÉBITO')
    conta = (precoProduto*0.95)
    desconto = conta - precoProduto
    print(f'COM 5% DE DESCONTO, TOTAL : {conta}')
    print(f'VALOR DO DESCONTO : {desconto}')
elif formaPagamento == 3:
    print('FORMA DE PAGAMENTO : 1X OU 2X CARTÃO DE CRÉDITO')
    print(f'SEM DESCONTO, TOTAL : {precoProduto}')
    print('SEM DESCONTO : 0')
else:
    print('FORMA DE PAGAMENTO : 3X MAIS NO CARTÃO DE CRÉDITO')
    conta = (precoProduto*1.20)
    juros = conta - precoProduto
    print(f'COM 20% DE JUROS, TOTAL : {conta}')
    print(f'VALOR DO JUROS : {juros}')