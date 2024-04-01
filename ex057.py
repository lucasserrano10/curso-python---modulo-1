numero = int(input('DIGITE UM NÚMERO :'))
i = numero - 1
somaF = 0
print(f'{numero} FATORIAL !')
while i != 1:
    c = numero*i
    numero = c
    i -= 1
    print(f'{numero}x{i}={numero*i}')
    print(f'resultado fatorial - {numero*i}')

