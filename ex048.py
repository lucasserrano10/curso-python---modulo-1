cont = 0
numero = int(input('DIGITE UM NÚMERO PARA VER SE É PRIMO :'))
for c in range(1,numero + 1):
    if numero % c == 0:
        print('\033[32m')
        print(c)
        cont += 1
    else:
        print('\033[31m')
        print(c)

if cont == 2:
    print('É PRIMO')
else:
    print('NÃO É PRIMO')