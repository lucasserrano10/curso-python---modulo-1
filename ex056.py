numero = int(input('DIGITE UM NÚMERO :'))
contador = numero - 1
somaF = 0
print(f'{numero} FATORIAL !')
while contador != 1:
    c = numero*contador
    numero = c
    contador -= 1
    print(f'{numero}x{contador}={numero*contador}')
print(f'resultado fatorial - {numero*contador}')

#DA PARA IMPORTAR DE MATH FATORIAL#