contadorNumeros = 0
somaNumeros = 0
numero = 0
while numero != 999:
    numero = int(input('DIGITE UM NÚMERO :'))
    if numero == 999:
        break
        print('FINISH')
    contadorNumeros += 1
    somaNumeros+= numero

print(f'O TOTAL DE NÚMEROS DIGITADOS FORAM {contadorNumeros}')
print(f'A SOMA DOS NÚMEROS FORAM {somaNumeros}')
print('FIM-999')