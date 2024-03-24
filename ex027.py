distancia = float(input('QUAL É A DISTÂNCIA DA VIAGEM EM KM ?'))

if distancia <= 200:
    print('PREÇO DA PASSAGEM :')
    preco = distancia * 0.45
    print(f'{preco}R$')
else :
    print('PREÇO DA PASSAGEM :')
    preco = distancia * 0.50
    print(f'{preco}R$')
