contadorTabuada = 1

n = 0
while not n < 0:
    contadorTabuada = 1
    n = int(input('QUER VER A TABUADA DE QUAL VALOR [<0, ENCERRA PROGRAMA] ?'))
    while n > 0:
        print(f'{n} X {contadorTabuada} = {n*contadorTabuada}')
        contadorTabuada += 1
        if contadorTabuada >= 11:
            break
print('FIM !')

