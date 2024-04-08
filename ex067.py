print(f'-=-'*30)
print('FAST SHOP')
print(f'-=-'*30)
somaCompra = 0
maisBarato = 0
maisMil = 0
contador = 0
preco = 0
produtoBarato = ''
while True:
    produto = str(input('NOME DO PRODUTO: '))
    preco = float(input('PREÇO: R$'))
    contador += 1
    somaCompra += preco
    if preco >= 1000:
        maisMil += 1
    if contador == 1:
        maisBarato = preco
        produtoBarato = produto
    else:
        if preco < maisBarato:
            maisBarato = preco
            produtoBarato = produto
    qrContinuar = input('QUER CONTINUAR [S/N]: ').strip().upper()
    if qrContinuar == 'N':
        break
print('------FIM DA COMPRA------')
print(f'TOTAL DA COMPRA: {somaCompra}')
print(f'PRODUTOS ACIMA DE 1000: {maisMil}')
print(f'PRODUTO MAIS BARATO {maisBarato}, NO QUAL É {produtoBarato}')

