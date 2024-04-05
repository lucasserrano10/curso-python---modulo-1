somaNumeros = 0
contadorNumeros = 0
n = 0
while n != 999:
    n = int(input('DIGITE UM NÚMERO [999 para parar]:'))
    if n == 999:
        break
    contadorNumeros += 1
    somaNumeros += n
print(f'-'*30)
print(f'A SOMA DOS NUMEROS DIGITADOS FORAM {somaNumeros}')
print(f'-'*30)
print(f'A QUANTIDADE DE NUMEROS DIGITADOS FORAM {contadorNumeros}')


