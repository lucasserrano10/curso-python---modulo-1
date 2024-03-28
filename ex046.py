somaPares = 0
for c in range(1,7):
    n = int(input('DIGITE UM NÚMERO :'))
    if n % 2 == 0:
        somaPares += n
print(f'A SOMA DOS {c} NÚMEROS PARES INFORMADOS SÃO : {somaPares}')